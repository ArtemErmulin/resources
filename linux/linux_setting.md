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

Сначала необходимо скачать `*.bundle` с [официального сайта VMWare](https://softwareupdate.vmware.com/cds/vmw-desktop/).

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

## Ошибка `vmmon`

There is a lot of posts about the missing vmmon, but this one always bites me after I update ubuntu kernel, and then I forget every time :)

From: https://kb.vmware.com/s/article/1002411

```bash
vmware-modconfig --console --install-all
```

EDIT- I also have to do the following now on Ubuntu:

"First line only needs to be run once:

```bash
openssl req -new -x509 -newkey rsa:2048 -keyout MOK.priv -outform DER -out MOK.der -nodes -days 36500 -subj "/CN=VMware/"
sudo mokutil --import MOK.der
```

Then reboot and if memory serves you will asked to confirm a change to your boot loader. Essentially you are adding this self created cert to the boot loader.

```bash
sudo /usr/src/linux-headers-uname -r/scripts/sign-file sha256 ./MOK.priv ./MOK.der $(modinfo -n vmmon)

sudo /usr/src/linux-headers-uname -r/scripts/sign-file sha256 ./MOK.priv ./MOK.der $(modinfo -n vmnet)

sudo modprobe -v vmmon

sudo modprobe -v vmnet

sudo vmware-networks --start
```

You need to have the very latest version of workstation/player/viewer if you upgrade your kernel Workstation builds modules, and often the build process breaks if there are kernel changes. So if you are having problems first make sure you have the latest version of workstation https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html

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

# Работа с пользователями
[Шпаргалка](https://www.dmosk.ru/miniinstruktions.php?mini=linux-users)

Добавление нового пользователя с правами администратора
```bash
sudo useradd usr -s /bin/bash -g sudo -d /home/username/
```

Удаление
```bash
sudo userdel -f username
```

Задание пароля
```bash
passwd username
```
