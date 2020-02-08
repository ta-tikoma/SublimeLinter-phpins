# SublimeLinter-phpins
This linter plugin for SublimeLinter provides an interface to phpins. It will be used with files that have the "PHP" syntax. For checking variable declarations and including classes, etc.

## Installation

1. Install [composer](https://getcomposer.org/).
2. Install `phpins` using below command:
```
composer global require ta-tikoma/phpins-cli
```
3. Make sure composer global bin directory is available in PATH or in SublimeLinter settings:
```
{
	"paths": {
        "linux": [
        	"~/.config/composer/vendor/bin"
        ]
    },
}
```

## Settings

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html


## Better

If you want to help me make this package better, then welcome: https://github.com/ta-tikoma/phpins
