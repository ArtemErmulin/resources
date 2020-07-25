# Установить заданное разрешение экрана (если linux устанавливается на виртуальную машину)

Введя в терминале следующую команду мы увидим список интерфейсов по которым могут быть подключены мониторы и доступные режимы работы монитора (разрешение и частота смена кадров в герцах).
```bash
$ xrandr
```
Если необходимого режима ещё не существует, то сначала вызываем утилиту `CVT` (Coordinated Video Timing) с необходимым разрешением и частотой кадров в качестве параметров (в качестве примера добавим режим 1920x1080 при 60Гц):
```bash
$ cvt 1920 1080 60
```
Далее мы скопируем всё, что после `Modeline` при вызове `xrandr` с ключём создания нового режима:
```bash
$ xrandr --newmode "1920x1080_60.00" 173.00 1920 2048 2248 2576  1083 1088 1120 -hsync +vsync
```
Теперь осталось "привязать" созданный режим к нужному интерфейсу (в нашем примере к `Virtual1`):
```bash
$ xrandr --addmode Virtual1 1920x1080_60.00
```
Наконец, мы можем выбрать нужное нам разрешение для монитора:
```bash
$ xrandr --output Virtual1 --mode 1920x1080_60.00
```
Для активации необходимых настроек при старте, создайте файл `~/.xprofile` (`~/` указывает на расположение в домашней директории) и внесите в него необходимые строки команд `xrandr`.
В случае, если после создание файла и перезагрузки системы заданное разрешение экрана не установилось, то следует зайти в настройки системы, выбрать необходимое разрешение экрана, подтвердить изменения и перезагрузить систему.

# VMWare Player

## Установка

Сначала необходимо скачать `*.bundle` с [официального сайта VMWare](www.yandex.ru).

После того как вы скачаете установщик, нужно установить заголовочные файлы ядра (если еще не установлены).

```bash
$ sudo apt install build-essential linux-headers-$(uname -r)
```

Первый вариант установки:

```bash
$ sudo apt install gksu
$ sudo gksudo bash ~/Downloads/VMware-Player-12.5.1-4542065.x86_64.bundle
```

Второй вариант установки:

```bash
$ sudo chmod +x ~/Downloads/VMware-Player-12.5.1-4542065.x86_64.bundle
$ sudo ~/Downloads/VMware-Player-12.5.1-4542065.x86_64.bundle
```

## Удаление

```bash
$ sudo vmware-installer -u vmware-player
```

# Консольные утилиты

## bashmarks
[GitHub](https://github.com/huyng/bashmarks)

```bash
$ git clone git://github.com/huyng/bashmarks.git
$ cd bashmarks
$ make install
```
Добавить строчку в файл `~/.bashrc` или `~/.bash_profile`
```bash
$ source ~/.local/bin/bashmarks.sh
```

## fzf
[GitHub](https://github.com/junegunn/fzf#usage)

# SSH
## Настройка
В папке ~/.ssh/ создать конфигурационный файл `config`, где можно прописать параметры всех SSH соединений:
```
Host host_name
  HostName host_name_ip
  user user_name
  IdentityFile path/to/ssh/pub/key
```
## Настройка доступа ssh без подтверждения пароля
Нужно указать в конфигурационном файле параметр `IdentityFile`, после скопировать свой публичный ключ на удаленный сервер командой:
```
ssh host_name 'cat >> ~/.ssh/authorized_keys' < ~/.ssh/id_rsa.pub
```

# Исправление работы WiFi
При периодическом отключении интернета через WiFi, выполнить команды:
- Get details of your PCI wireless card by running the following
```bash
sudo lshw -class network
```
- Get your card model info according to the product line of the wireless interface. For instance, as you can see in the question description it says product: `RTL8723BE PCIe Wireless Network Adapter` so the model of my card is `RTL8723BE`

- Open or create `/etc/pm/config.d/config` and add `SUSPEND_MODULES="rtl8723be"` (replace `rtl8723be` with your own model number) Then run
```bash
echo "options rtl8723be fwlps=N" | sudo tee /etc/modprobe.d/rtl8723be.conf
```
and reboot.

# Исправление работы разъёма для наушников (на ноутбуке)
[Headphone jack not working?](https://askubuntu.com/a/831453/1109255)
