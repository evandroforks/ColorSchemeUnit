# WHAT COLOR SCHEME UNIT IS

A testing framework for Sublime Text color schemes.

[![Build Status](https://img.shields.io/travis/gerardroche/sublime-color-scheme-unit/master.svg?style=flat-square)](https://travis-ci.org/gerardroche/sublime-color-scheme-unit) [![Build status](https://img.shields.io/appveyor/ci/gerardroche/sublime-color-scheme-unit/master.svg?style=flat-square)](https://ci.appveyor.com/project/gerardroche/sublime-color-scheme-unit/branch/master) [![Coverage Status](https://img.shields.io/coveralls/gerardroche/sublime-color-scheme-unit/master.svg?style=flat-square)](https://coveralls.io/github/gerardroche/sublime-color-scheme-unit?branch=master) [![Minimum Sublime Version](https://img.shields.io/badge/sublime-%3E%3D%203.0-brightgreen.svg?style=flat-square)](https://sublimetext.com) [![Latest Stable Version](https://img.shields.io/github/tag/gerardroche/sublime-color-scheme-unit.svg?style=flat-square&label=stable)](https://github.com/gerardroche/sublime-color-scheme-unit/tags) [![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-color-scheme-unit.svg?style=flat-square)](https://github.com/gerardroche/sublime-color-scheme-unit/stargazers) [![Downloads](https://img.shields.io/packagecontrol/dt/ColorSchemeUnit.svg?style=flat-square)](https://packagecontrol.io/packages/ColorSchemeUnit) [![Author](https://img.shields.io/badge/twitter-gerardroche-blue.svg?style=flat-square)](https://twitter.com/gerardroche)

Many color schemes available for Sublime Text are not kept up to date, don't support plugins, use too many variants of the same colors, or only exist to be compatible with a specific theme. They tend to go out of date and break in unexpected and unknown ways. [ColorSchemeUnit](https://github.com/gerardroche/sublime-color-scheme-unit), which is a testing framework for Sublime Text color schemes, helps improve the quality of color schemes and prevent regressions.

![Screenshot](screenshot.png)

## OVERVIEW

* [Installation](#installation)
* [Commands](#commands)
* [Keybindings](#key-bindings)
* [Configuration](#configuration)
* [Testing](#testing)
* [Changelog](#changelog)
* [License](#license)


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

Key | Description
--- | -----------
`F4` | Jump to Next Failure
`Shift+F4` | Jump to Previous Failure

*You can also use the [Test](https://github.com/gerardroche/sublime-test) plugin, which unifies ST testing plugin key bindings.*

## CONFIGURATION

Key | Description | Type | Default
----|-------------|------|--------
`color_scheme_unit.debug` | Enable debug messages. | `boolean` | `false`
`color_scheme_unit.coverage` | Enable coverage report. | `boolean` | `true`

`Menu > Preferences > Settings - User`

```json
{
    "color_scheme_unit.debug": true,
    "color_scheme_unit.coverage": true
}
```

## Testing

When building a color scheme, rather than manually checking the styles, you can define a color scheme test file that will do the checking for you:


```text
// COLOR SCHEME TEST "MonokaiFree/MonokaiFree.tmTheme" "C"

#include <windows.h>
// ^^^^^ fg=#f92672 fs=
//       ^^^^^^^^^^^ fg=#e6db74 fs=

typedef int myint;
// ^^^^ fg=#66d9ef fs=italic
//      ^^^ fg=#66d9ef fs=italic
//          ^^^^^ fg=#a6e22e fs=
//               ^ fg=#f8f8f2 fs=

int main(int argc, char **argv) {}
//  ^^^^ fg=#a6e22e fs=
//      ^ fg=#f8f8f2 fs=
//       ^^^ fg=#66d9ef fs=italic
//           ^^^^ fg=#fd971f fs=italic
//               ^ fg=#f8f8f2 fs=
//                 ^^^^ fg=#66d9ef fs=italic
//                      ^^ fg=#f92672 fs=
//                        ^^^^ fg=#fd971f fs=italic
//                            ^ fg=#f8f8f2 fs=
//                              ^^ fg=#f8f8f2 fs=
```

Tests are similar to [syntax tests](https://www.sublimetext.com/docs/3/syntax.html). To make one, follow these rules:

1. Ensure the file name starts with `color_scheme_test`.
2. Ensure the file is saved somewhere within the Packages directory: next to the corresponding .sublime-syntax file is a good choice.
3. Ensure the first line of the file starts with: `<comment_token> COLOR SCHEME TEST "<color_scheme>" [SKIP IF NOT ]"<syntax>"`. Note that `[SKIP IF NOT ]` is optional.
4. Test files must use spaces (not tabs).

Here is a suggested project layout:

    .
    ├── Name.tmTheme
    └── tests
      ├── color_scheme_test.css
      ├── color_scheme_test.html
      ├── color_scheme_test.js
      ├── color_scheme_test.json
      └── ...

Once the above conditions are met, running a test command from the Command Palette with a color scheme test or color scheme file selected will run the tests, and show the results in an output panel. *Next Result* (`F4`) can be used to navigate to the first failing test.

Each test in the color scheme test file must first start the comment token (established on the first line, it doesn't have to be a comment according to the syntax), and then a `^` token.

There is one type of test:

Caret: `^` this will test the following selector against the scope on the most recent non-test line. It will test it at the same column the `^` is in. Consecutive `^`'s will test each column against the selector. Assertions are specified after the caret.

There are four types of assertions:

Description | Examples
----------- | --------
Foreground color | `fg=#f8f8f2`
Background color | `bg=#272822`
Font style (space delimited list) | `fs=italic`, `fs=italic bold`
Sublime Text build version (only `>=` constraint is supported) | `build>=3127`

One or more assertions are required, and they *must be specified in the order*: `fg`, `bg`, `fs`, and `build`. Here are some examples of valid assertions:

```text
def somefunc(param1='', param2=0):
# ^ fg=#66d9ef
# ^ bg=#272822
# ^ fs=italic
# ^ fg=#66d9ef bg=#272822
# ^ fg=#66d9ef bg=#272822 fs=italic bold
# ^ fg=#66d9ef bg=#272822 fs=italic build>=3127
```

**Examples**

An example testing the Python syntax in MonokaiFree color scheme.

```text
# COLOR SCHEME TEST "MonokaiFree/MonokaiFree.tmTheme" "Python" # flake8: noqa

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

An example testing the HTML syntax in MonokaiFree color scheme.

```text
<!-- COLOR SCHEME TEST "MonokaiFree/MonokaiFree.tmTheme" "HTML" -->
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

An example testing the PHP syntax in MonokaiFree color scheme.

```text
<?php // COLOR SCHEME TEST "MonokaiFree/MonokaiFree.tmTheme" "PHP"

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

An example testing the Syntax Highlighting for Sass package SCSS syntax in MonokaiFree color scheme. This package is not provided by Sublime Text by default, so we've made it optional by specifying "SKIP IF NOT". Thus allows the tests to pass even if the package is not installed.

```
/* COLOR SCHEME TEST "MonokaiFree/MonokaiFree.tmTheme" SKIP IF NOT "Syntax Highlighting for Sass/SCSS"

    Tests for Syntax Highlighting for Sass package:
    https://packagecontrol.io/packages/Syntax%20Highlighting%20for%20Sass

*/

        /* This indented comment is to the preceding whitespace. */
/* ^ fg=#f8f8f2 bg=#272822 fs= */

    /* x */
/*  ^^^^^^^ fg=#75715e bg=#272822 fs= */

    body {}
/*  ^^^^ fg=#f92672 fs= */
/*       ^^ fg=#f8f8f2 fs= */

    #id {}
/*  ^^^ fg=#fd971f fs= */
/*      ^^ fg=#f8f8f2 fs= */

    .class {}
/*  ^^^^^^ fg=#a6e22e fs= */
/*         ^^ fg=#f8f8f2 fs= */

    @font-face {}
/*  ^^^^^^^^^^ fg=#f92672 fs= */
/*             ^^ fg=#f8f8f2 fs= */
```

Explore the [MonokaiFree](https://github.com/gerardroche/sublime-monokai-free) color scheme test suite for detailed examples.

## CONTINUOUS INTEGRATION

### Travis CI

```yaml
language: python

env:
    global:
        - PACKAGE="MonokaiFree"
    matrix:
        - SUBLIME_TEXT_VERSION="3"

matrix:
    include:
        - os: linux
          python: 3.3

before_install:
    - curl -OL https://raw.githubusercontent.com/randy3k/UnitTesting/master/sbin/appveyor.ps1

install:
    - sh travis.sh bootstrap
    - sh travis.sh install_color_scheme_unit

script:
    - sh travis.sh run_color_scheme_tests --coverage

notifications:
    email: false
```

### AppVeyor

```yaml
environment:
    global:
        PACKAGE: "MonokaiFree"
        SUBLIME_TEXT_VERSION: "3"

clone_depth: 5

install:
    - ps: appveyor DownloadFile "https://raw.githubusercontent.com/randy3k/UnitTesting/master/sbin/appveyor.ps1"
    - ps: .\appveyor.ps1 "bootstrap" -verbose
    - ps: .\appveyor.ps1 "install_color_scheme_unit" -verbose

build: off

test_script:
    - ps: .\appveyor.ps1 "run_color_scheme_tests" -coverage
```

More documentation can be found in the [UnitTesting](https://github.com/randy3k/UnitTesting) documentation.

You can also explore the [MonokaiFree](https://github.com/gerardroche/sublime-monokai-free) for example usage.

## CHANGELOG

See [CHANGELOG.md](CHANGELOG.md).

## LICENSE

Released under the [BSD 3-Clause License](LICENSE).
