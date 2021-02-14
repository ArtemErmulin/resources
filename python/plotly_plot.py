"""
Для отрисовки графика используя библиотеку Plotly.
"""
import pandas as pd

import plotly
import plotly.graph_objs as go
import plotly.io as pio
from plotly.offline import init_notebook_mode, iplot, plot


def plot_plotly(
    dataf: pd.DataFrame,
    col_names=None,
    title="",
    labels=None,
    x_label="",
    y_label="",
    file_name="1.html",
    mode_line="lines",
    in_jnb=False,
    legend=None,
    multiaxis=False,
    automodeline=True,
    width=None,
    height=None,
    auto_open=True,
    annotations=None,
    y2_label="",
    linewiths=None,
    x_range=None,
    y_range=None,
    png_name=None,
):
    """
    Функция строит графики, используя библиотеку 'plotly'.

    Parameters:
    -----------
        dataf -- данные, для построения графика (тип pandas.DataFrame)

        col_names -- названия столбцов, которые необходимо отобразить
        (по умолчанию все столбцы)

        title -- название графика (по умолчанию '')

        labels -- легенда (передается списком, по умолчанию '')

        x_label -- название оси 'X' (по умолчанию '')

        y_label -- название оси 'Y' (по умолчанию '')

        file_name -- название файла (по умолчанию '', с сохранением в рабочую
        директорию)

        mode_line -- тип линий (лист, или одно значение)
        возможные значения:'line' - линия, 'markers' - маркеры

        in_jnb -- 'IN_JupyterNoteook' параметр определяет где будет
        выводиться график: в строке (для Jupyter Notebook),
        или в отдельный файл

        multiaxis -- параметр, показывающий необходимо ли,
        каждый график выводить на отдельной оси 'y' (только для двух линий!)

        automodeline -- параметр, включающий атоматическое определение
        типа линий (маркер, в случае отсутствия у значений графика более 40%
        от длины всего датафрейма)

        auto_open -- необходимо ли открыть график после создания.

    Returns:
    --------
        График в формате html, или график в Jupyter Notebook.

    """
    annotations = annotations or []
    linewiths = linewiths or [2]
    x_range = x_range or []
    y_range = y_range or []

    if not isinstance(dataf, pd.DataFrame):
        raise ValueError("`dataf` is not pd.DataFrame.")

    # проверяем названия столбцов (по умолчанию строим по всем столбцам)
    if not col_names:
        col_names = dataf.columns

    # если список легенды не был передан, генерим список
    # необходимой длины
    if not labels:
        labels = col_names

    # определяем тип линий
    # если параметр автоматического определения типа линий включен
    if automodeline:
        mode_line = []
        # для всех столбцов, если количество значений мень 60%, то маркер
        # иначе линия
        for colname in col_names:
            if len(dataf[colname].dropna()) / len(dataf) < 0.6:
                mode_line.append("markers")
            else:
                mode_line.append("lines")
    # если параметр атоматического определения типа линии выключен
    elif len(col_names) > 1 and len(mode_line) != len(col_names):
        mode_line = mode_line * len(col_names)

    # проверить, необходимо ли построить график на двух разных осях y
    if multiaxis:
        if len(col_names) > 2:
            raise ValueError("Required number of multiaxis is 2")

        yaxis = ["y", "y2"]

    else:
        yaxis = ["y"] * len(col_names)

    if len(linewiths) != len(col_names):
        linewiths = [2] * len(col_names)

    # помещаем в переменную 'data' все данные из dataf
    data = []
    for col, m_line, label, y_axis, linewith in zip(
        col_names, mode_line, labels, yaxis, linewiths
    ):
        data.append(
            go.Scatter(
                x=dataf.index,
                y=dataf[col],
                mode=m_line,
                line=dict(width=linewith),
                marker=dict(size=5),
                name=label,
                yaxis=y_axis,
            )
        )

    # параметры осей
    layout = dict(
        title=title,
        xaxis=dict(title=x_label),  # range=x_range),
        yaxis=dict(title=y_label),  # range=y_range),
        yaxis2=dict(overlaying="y", side="right", title=y2_label),
        annotations=annotations,
    )

    if x_range:
        layout["xaxis"]["range"] = x_range

    if y_range:
        layout["yaxis"]["range"] = y_range

    if width:
        layout["width"] = width

    if height:
        layout["height"] = height

    if legend:
        layout["legend"] = legend

    # создаем фигуру
    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(legend_orientation="h")

    # проверяем, где необходимо построить график:
    # в строке, или сохранить в файл
    if in_jnb:
        # случае, если функция была вызвана из Jupyter
        # для отрисовки графика inline,
        # необходимо подклюить режим notebook
        init_notebook_mode(connected=True)
        iplot(fig, show_link=False, config={"scrollZoom": True})

    # если указано название имени картинок в формате `*.png`
    elif png_name:
        pio.write_image(fig, png_name, width=800, height=500)

    else:
        plot(fig, filename=file_name, auto_open=auto_open, config={"scrollZoom": True})
