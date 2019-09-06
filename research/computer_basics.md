# Setting Up a Computer Environment for Research

## Terminal Tools

### Terminal Emulator

* [__iTerm2__ - macOS Terminal Replacement](https://www.iterm2.com/)
	- A nice free choice for __MacOSX__. [__iTerm2__](https://github.com/gnachman/iTerm2) brings the terminal into the modern age with features you never knew you always wanted.
	- A [cheat sheet of iTerm2 shortcuts](https://gist.github.com/squarism/ae3613daf5c01a98ba3a)

* It becomes easier and easier to do research under Windows system:
	- [Microsoft's terminal - The new Windows Terminal, and the original Windows console host](https://github.com/microsoft/terminal)
	- [__cmder__ - Portable console emulator for Windows](https://cmder.net/)

* Different Linux releases have there own default terminal emulator and normally they are good enough for research works. Meanwhile, there are some nice choices of drop-down style emulators:
	- [__tilda__ - A Gtk based drop down terminal for Linux and Unix](https://github.com/lanoxx/tilda)
	- [__guake__ - Drop-down terminal for GNOME](https://github.com/Guake/guake)
		- __Guake__ is a dropdown terminal made for the __GNOME__ desktop environment. __Guake__'s style of window is based on an FPS game, and one of its goals is to be easy to reach.

### Terminal Multiplexer

* [__GNU Screen__](http://git.savannah.gnu.org/cgit/screen.git)
	- __Screen__ is available in most Unix/Linux system release.
	- [How to use Linux Screen](https://linuxize.com/post/how-to-use-linux-screen/)

* [__tmux__ - a terminal multiplexer for Unix-like operating systems](https://github.com/tmux/tmux)
	- Similar to __Screen__. There are a lot of discussions about the pros and cons of __Screen__ and __tmux__, but as a beginner, either is fine.
	- Read [A __tmux__ crash course](https://thoughtbot.com/blog/a-tmux-crash-course) and [__tmux__ shortcuts and cheat sheet](https://gist.github.com/MohamedAlaa/2961058) before you use it.

## Shell Environment

> Fluency on the command line is a skill often neglected or considered arcane, but it improves your flexibility and
> productivity as an engineer in both obvious and subtle ways.  -- The Art of Command Line

* **The same also applies to student of science and researcher.**

* [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line)
	- In multiple languages, including Chinese

* [37 Important Linux Commands You Should Know](https://www.howtogeek.com/412055/37-important-linux-commands-you-should-know/)

* [__awesome-command-line-apps__ - Use your terminal shell to do awesome things](https://github.com/herrbischoff/awesome-command-line-apps)
	- A curated list of useful command line apps, in celebration of the TUI.

* [__awesome-macos-command-line__ - Use your macOS terminal shell to do awesome things](https://github.com/herrbischoff/awesome-macos-command-line)
	- A curated list of shell commands and tools specific to OS X.
	- A lot of these actually work for Linux too.

### Regular Expression

* Regular expression (__regex__) is a group of characters or symbols which is used to find a specific pattern from a text. It is very useful to learn the basic of __regex__.

* [Learn Regex the Easy Way](https://github.com/ziishaned/learn-regex)
	- There is a [Chinese version](https://github.com/ziishaned/learn-regex/blob/master/translations/README-cn.md)

### __Bash__ related

* [Pure Bash Bible](https://github.com/dylanaraps/pure-bash-bible)
	- A collection of pure bash alternatives to external processes.

* [Bash Notebook](https://github.com/denysdovhan/bash-handbook)
	- In depth Bash notebook in multiple languages

* [__Bash-it__ - a collection of community Bash commands and scripts for Bash 3.2+](https://github.com/Bash-it/bash-it)
	- Achieve some of __zsh__'s functions in __bash__.

### Other than __bash__

* [Oh My Zsh](https://ohmyz.sh/)
	- Code on Github is [here](https://github.com/robbyrussell/oh-my-zsh/)

* [The Fish Cookbook](https://github.com/jorgebucaran/fish-cookbook)
	- Tips and recipes for fish, from shell to plate

## Version Control

### __Git__

* [__git__](https://git-scm.com/doc) is the most widely used software for version control and it is extremely useful to learn the basic of it.
	- Plenty of reference and examples are provided in the above webpage including many short videos.

* [Learn Git with Bitbucket Cloud](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud) is another good place to start learning about version control using __git__.
	- [Git cheat sheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet) and [Advanced Git Tutorials](https://www.atlassian.com/git/tutorials/advanced-overview).

* [Oh shit, git!](http://ohshitgit.com/)
	- A very practical guide for when you screw up in __git__.

### Others

* [__mercurial__](https://www.mercurial-scm.org/) is another popular version control software.

## System Tools

* [__gotop__ - system monitor](https://github.com/cjbassi/gotop)
	- A terminal based graphical activity monitor inspired by gtop and vtop

* [__tldr__ - command document for human](https://github.com/tldr-pages/tldr)
	- Simplified and community-driven man pages

* [__thefuck__ - Magnificent app which corrects your previous console command](https://github.com/nvbn/thefuck)
	- Well....it is actually kind of useful...

-----

## MacOS

* [__mac-setup__: Installing Development environment on macOS](https://github.com/sb2nov/mac-setup)
	- The more readable website is [here](http://sourabhbajaj.com/mac-setup/iTerm/tree.html)

### Mount harddrive in Linux file system

* Linux system uses __ext4__ or other similar file system that is not automatically readable under __MacOSX__. The [__ext4fuse__ software](https://github.com/gerard/ext4fuse) will be useful.
	- Please read [this stackexchange thread](https://apple.stackexchange.com/questions/210198/mount-ext4-on-el-capitan) for more details.

* [__ExtFS__](https://www.paragon-software.com/us/home/extfs-mac/) is not a free software. It costs you $39.95 but it is claimed to be able to mount or even repair __ext__ system under __MacOSX__