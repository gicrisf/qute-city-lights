# Qutebrowser City Lights

> A matte dark theme for Qutebrowser.

<!-- Screenshot here -->

## Install
You could dump off the content of `city-lights-theme.py` in your `config.py` file and it would be effective enough, but here after I will suggest you the tidy way to install a qutebrowser theme.

Make a themes directory in your dot qutebrowser one. Let's say you keep your `config.py` in `~/.config/qutebrowser`:

``` sh
mkdir ~/.config/qutebrowser/themes
```

Then, clone this repo in the new themes directory.

``` sh
git clone https://github.com/gicrisf/qute-city-lights.git ~/.config/qutebrowser/themes/qute-city-lights
```

Add `config.source('themes/qute-city-lights/city-lights-theme.py')` in your `config.py` file.

N.B. Make sure you don't mess up with colors after importing it (e.g. by leaving another theme import after this command).

Enjoy your new dark theme.

## Support
Why don't you help me keeping myself awake buying me a coffee?
I will use the extra time to write more code!

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/V7V425BFU)

<a href="https://liberapay.com/gicrisf/donate"><img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg"></a>

## License
[MIT](https://github.com/gicrisf/qute-city-lights/blob/main/LICENSE)
