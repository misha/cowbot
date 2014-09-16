cowbot [![Build Status](https://travis-ci.org/msoliter/cowbot.svg?branch=master)](https://travis-ci.org/msoliter/cowbot)
======

The cowbot takes directives in reddit comments and replies with a styled comment.

Usage
-----

The most simple directive is ```@cowbot```, which renders that comment's parent's content in a random ASCII actor.

You can also specify which actor to use with ```@cowbot:actor```. Available actors may be referenced by name from the [cowpy](https://github.com/jeffbuttars/cowpy) README. If the bot can't figure out what you want or you supply an invalid actor key, it'll just print up a random actor anyway.

Example Response
----------------

Generated with ```@cowbot:Stegosaurus```:

```
     ______________________________________________ 
    / import antigravity                           \
    | that was a code block                        |
    |                                              |
    |     from antigravity import xkcd             |
    |     this is a continuation of the code block |
    \                                              /
     ---------------------------------------------- 
    \                             .       .
     \                           / `.   .' " 
      \                  .---.  <    > <    >  .---.
       \                 |    \  \ - ~ ~ - /  /    |
             _____          ..-~             ~-..-~
            |     |   \~~~\.'                    `./~~~/
           ---------   \__/                        \__/
          .'  O    \     /               /       \  " 
         (_____,    `._.'               |         }  \/~~~/
          `----.          /       }     |        /    \__/
                `-.      |       /      |       /      `. ,~~|
                    ~-.__|      /_ - ~ ^|      /- _      `..-'   
                         |     /        |     /     ~-.     `-. _  _  _
                         |_____|        |_____|         ~ - . _ _ _ _ _>

^[```cowbot/1.0```](https://github.com/msoliter/cowbot)
```
