# ColorSchemeUnit

A testing framework for Sublime Text color schemes.

[![Continuous Integration](https://github.com/gerardroche/sublime-color-scheme-unit/actions/workflows/ci.yml/badge.svg)](https://github.com/gerardroche/sublime-color-scheme-unit/actions/workflows/ci.yml) [![codecov](https://codecov.io/gh/gerardroche/sublime-color-scheme-unit/branch/master/graph/badge.svg?token=Ln3mldFyPv)](https://codecov.io/gh/gerardroche/sublime-color-scheme-unit) ![Package Control](https://img.shields.io/packagecontrol/dt/ColorSchemeUnit)

![ColorSchemeUnit](screenshot.png)

## Setup

Install [ColorSchemeUnit](https://packagecontrol.io/packages/ColorSchemeUnit) via Package Control.

## Commands

<<<<<<< HEAD
Command | Description
:------ |:-----------
ColorSchemeUnit:&nbsp;Test&nbsp;Suite | Run test suite of the current file.
ColorSchemeUnit:&nbsp;Test&nbsp;File | Run tests for the current file.
ColorSchemeUnit:&nbsp;Show&nbsp;Styles | Show styles at the current cursor position.
ColorSchemeUnit:&nbsp;Generate&nbsp;Assertions | Generates assertions at the current cursor position.

## Key Bindings
=======

## Installation

### By Package Control

1. Download & Install **`Sublime Text 3`** (https://www.sublimetext.com/3)
1. Go to the menu **`Tools -> Install Package Control`**, then,
    wait few seconds until the installation finishes up
1. Now,
    Go to the menu **`Preferences -> Package Control`**
1. Type **`Add Channel`** on the opened quick panel and press <kbd>Enter</kbd>
1. Then,
    input the following address and press <kbd>Enter</kbd>
    ```
    https://raw.githubusercontent.com/evandrocoan/StudioChannel/master/channel.json
    ```
1. Go to the menu **`Tools -> Command Palette...
    (Ctrl+Shift+P)`**
1. Type **`Preferences:
    Package Control Settings – User`** on the opened quick panel and press <kbd>Enter</kbd>
1. Then,
    find the following setting on your **`Package Control.sublime-settings`** file:
    ```js
    "channels":
    [
        "https://packagecontrol.io/channel_v3.json",
        "https://raw.githubusercontent.com/evandrocoan/StudioChannel/master/channel.json",
    ],
    ```
1. And,
    change it to the following, i.e.,
    put the **`https://raw.githubusercontent...`** line as first:
    ```js
    "channels":
    [
        "https://raw.githubusercontent.com/evandrocoan/StudioChannel/master/channel.json",
        "https://packagecontrol.io/channel_v3.json",
    ],
    ```
    * The **`https://raw.githubusercontent...`** line must to be added before the **`https://packagecontrol.io...`** one, otherwise,
      you will not install this forked version of the package,
      but the original available on the Package Control default channel **`https://packagecontrol.io...`**
    > [!WARNING]
    > Placing this custom channel before the default channel changes Package Control's resolution globally.
    > Packages from this channel with the same name will override versions from the default channel.
    >
    > You can review the channel contents here:
    > https://raw.githubusercontent.com/evandrocoan/StudioChannel/master/channel.json
1. Now,
    go to the menu **`Preferences -> Package Control`**
1. Type **`Install Package`** on the opened quick panel and press <kbd>Enter</kbd>
1. Then,
    search for **`ColorSchemeUnit`** and press <kbd>Enter</kbd>

See also:

1. [ITE - Integrated Toolset Environment](https://github.com/evandrocoan/ITE)
1. [Package control docs](https://packagecontrol.io/docs/usage) for details.


## COMMANDS

*The [Test](https://github.com/gerardroche/sublime-test) plugin is recommended to unify testing commands and keymaps.*

Command Palette | Command | Description
--------------- | ------- | -----------
`:TestSuite` | `color_scheme_unit_test_suite` | Run test suite of the current file.
`:TestFile` | `color_scheme_unit_test_file` | Run tests for the current file.
`:TestResults` | `color_scheme_unit_test_results` | Show the test results panel.
`:ShowScopeAndColors` | `color_scheme_unit_show_scope_name_and_styles` | Show the scope name and applied colors of scheme at point under cursor.
`:InsertAssertions` | `color_scheme_unit_insert_assertions` | Inserts assertions for the current line.
`:InsertSyntaxAssertions` | `color_scheme_unit_insert_syntax_assertions` | Inserts syntax assertions for the current line.


## KEY BINDINGS

*The [Test](https://github.com/gerardroche/sublime-test) plugin is recommended to unify testing commands and keymaps.*

Add your preferred key bindings:

`Menu > Preferences > Key Bindings`

```json
[
    { "keys": ["ctrl+shift+a"], "command": "color_scheme_unit_test_suite" },
    { "keys": ["ctrl+shift+f"], "command": "color_scheme_unit_test_file" },
    { "keys": ["ctrl+shift+r"], "command": "color_scheme_unit_test_results" },
    { "keys": ["ctrl+shift+alt+p"], "command": "color_scheme_unit_show_scope_name_and_styles" },
    { "keys": ["ctrl+a"], "command": "color_scheme_unit_insert_assertions" },
    { "keys": ["ctrl+f"], "command": "color_scheme_unit_insert_syntax_assertions" },
]
```

Key bindings provided by default:
>>>>>>> master

Key | Description
--- | -----------
`f4` | Jump to Next Failure
`shift+f4` | Jump to Previous Failure

## Settings

Setting | Description | Type | Default
:-------|:------------|:-----|:-------
`color_scheme_unit.coverage` | Enable coverage report. | `boolean` | `false`
`color_scheme_unit.debug` | Enable debug messages. | `boolean` | `false`

Menu → Preferences → Settings

```js
"color_scheme_unit.debug": true,
"color_scheme_unit.coverage": true,
```

## Usage

Tests are similar to Sublime Text [syntax tests](https://www.sublimetext.com/docs/3/syntax.html). Here is an

```c
// COLOR SCHEME TEST "MonokaiFree.sublime-color-scheme" "C"

#include <windows.h>
// ^^^^^ fg=#f92672 fs=
//       ^^^^^^^^^^^ fg=#e6db74 fs=

typedef int myint;
// ^^^^ fg=#66d9ef fs=italic
//      ^^^ fg=#66d9ef fs=italic
//          ^^^^^ fg=#a6e22e fs=
//               ^ fg=#f8f8f2 fs=
```

### Tests

#### File names

Test must begin `color_scheme_test` e.g. `color_scheme_test.css`, `color_scheme_test.php`, `color_scheme_test.rb`.

The recommended package layout:

```sh
.
├── Monokai.sublime-color-scheme
└── tests/
  ├── color_scheme_test.css
  ├── color_scheme_test.php
  ├── color_scheme_test.rb
  └── ...
```

#### Headers

The first line must start:

```
<begin-comment> COLOR SCHEME TEST "<color-scheme>" "<syntax>"
```

Parameter | Description
:-------- | :----------
`<begin-comment>` | Any syntax comment e.g. `//`, `<!--`, `/**`, `#`, `--`
`<color-scheme>` | Name or resource path to color scheme.
`<syntax>` | Name or resource path to syntax.

Examples:

```rb
// COLOR SCHEME TEST "MonokaiFree.sublime-color-scheme" "Ruby"
```

```rb
// COLOR SCHEME TEST "Packages/MonokaiFree/MonokaiFree.sublime-color-scheme" "Ruby"
```

#### Conditional syntaxes

If a syntax may not exist, e.g. testing third party syntax support, use the `SKIP IF NOT` keywords and if the the syntax doesn't exist the test will be skipped instead of failing.

```rb
// COLOR SCHEME TEST "Monokai.sublime-color-scheme" SKIP IF NOT "Vue"
```

#### Whitespace

Test files must use spaces.

#### Assertions

Each assertion in the color scheme test file must first start the comment token, and then a `^` (caret) token. `^` this will assert against the scope on the most recent non-test line. It will test it at the same column as the `^`. Consecutive `^`'s will test each column. What to assert is specified after the caret.

Assertion | Example
:-------- | :------
Foreground color | `fg=#f8f8f2`
Background color | `bg=#272822`
Font style (space delimited list) | `fs=italic`, `fs=italic bold`
Sublime Text build version (only `>=` constraint is supported) | `build>=3127`

```rb
def somefunc(param1='', param2=0):
# ^ fg=#66d9ef
# ^ bg=#272822
# ^ fs=italic
# ^ fg=#66d9ef bg=#272822
# ^ fg=#66d9ef bg=#272822 fs=italic bold
# ^ fg=#66d9ef bg=#272822 fs=italic build>=3127
```

For more usage examples, the MonokaiFree color scheme has an [extensive test suite](https://github.com/gerardroche/sublime-monokai-free/tests).

#### Python example

```py
# COLOR SCHEME TEST "MonokaiFree.sublime-color-scheme" "Python"

import os
# ^ fg=#f8f8f2 bg=#272822 fs=
#  ^^^ fg=#f92672 fs=
#      ^^ fg=#f8f8f2

def f_name(arg1='', arg2=0):
# ^ fg=#66d9ef fs=italic
#   ^^^^^^ fg=#a6e22e fs=
#          ^ fg=#fd971f fs=italic
#              ^ fg=#f92672 fs=
#               ^^ fg=#e6db74 fs=
#                 ^ fg=#f8f8f2 fs=
#                   ^ fg=#fd971f fs=italic
#                       ^ fg=#f92672 fs=
#                        ^ fg=#ae81ff fs=
    if arg1 > arg2: # interesting
    #   ^ fg=#f92672 fs=
    #           ^ fg=#f92672 fs=
        print 'Gre\'ater'
        # ^ fg=#f92672 fs=
        #     ^^^^ fg=#e6db74 fs=
        #         ^^ fg=#ae81ff fs=
        #           ^^^^^ fg=#e6db74 fs=
```

#### HTML example

```html
<!-- COLOR SCHEME TEST "MonokaiFree.sublime-color-scheme" "HTML" -->
<!DOCTYPE html>
<!-- ^^^^ fg=#f92672 fs= -->
<!--      ^^^^^ fg=#f8f8f2 fs= -->
<html>
    <head>

        <meta charset="utf-8">
<!--    ^ fg=#f8f8f2 fs= -->
        <!--^ fg=#f92672 fs= -->
        <!--  ^ fg=#a6e22e fs= -->
        <!--         ^ fg=#f8f8f2 fs= -->
        <!--           ^ fg=#e6db74 fs= -->
        <!--                 ^ fg=#f8f8f2 fs= -->
    </head>
    <body>
        <p class="title" id='title'>Title</p>
    <!-- ^ fg=#f92672 fs= -->
        <!-- ^ fg=#a6e22e fs= -->
        <!--    ^ fg=#f8f8f2 fs= -->
        <!--     ^^^^^^^ fg=#e6db74 fs= -->
        <!--             ^^ fg=#a6e22e fs= -->
        <!--               ^ fg=#f8f8f2 fs= -->
        <!--                ^^^^^^^ fg=#e6db74 fs= -->
        <!--                       ^ fg=#f8f8f2 fs= -->
        <!--                               ^ fg=#f92672 fs= -->
        <!--                                ^ fg=#f8f8f2 fs= -->

    </body>
<!--  ^ fg=#f92672 fs= -->
</html>
<!-- ^ fg=#f92672 fs= -->
```

#### PHP example

```php
<?php // COLOR SCHEME TEST "MonokaiFree.sublime-color-scheme" "PHP"

use \Psr\Http\Message\ServerRequestInterface as Request;
//^ fg=#f92672 fs=
//  ^^^^^^^^^^^^^^^^^^ fg=#f8f8f2 fs=
//                    ^^^^^^^^^^^^^^^^^^^^^^ fg=#66d9ef fs=italic
//                                           ^^ fg=#f92672 fs=
//                                              ^^^^^^^ fg=#a6e22e fs=
//                                                     ^ fg=#f8f8f2 fs=
use \Psr\Http\Message\ResponseInterface as Response;
//^ fg=#f92672 fs=
//  ^^^^^^^^^^^^^^^^^^ fg=#f8f8f2 fs=
//                    ^^^^^^^^^^^^^^^^^ fg=#66d9ef fs=italic
//                                      ^^ fg=#f92672 fs=
//                                         ^^^^^^^^ fg=#a6e22e fs=
//                                                 ^ fg=#f8f8f2 fs=

require 'vendor/autoload.php';
// ^^^^ fg=#f92672 fs=
//      ^^^^^^^^^^^^^^^^^^^^^ fg=#e6db74 fs=
//                           ^ fg=#f8f8f2 fs=
```

## CI

To run tests in CI see [UnitTesting](https://github.com/randy3k/UnitTesting) documentation.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [GPL-3.0-or-later License](LICENSE).
