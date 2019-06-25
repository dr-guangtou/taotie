# 如何正确的踏上科研的不归路

<img src="http://www.phdcomics.com/comics/archive/phd051017s.gif" width="80%">

## 动机与使命

* To become a scientist is to dive into the unknown on behalf of the human-kind, it is never an easy job but can be very rewarding as well.  It is good idea to always check your motivation, think about your mission statement, and confront your career and personal choices sincerely.
* [Choose Your Own Adventure: Developing A Values-Oriented Framework for Your Career by Lucianne Walkowicz](https://arxiv.org/abs/1805.09963)
    - I think you should read this, every word of it, before you read anything else.  This is probably the best career advice I have ever read.  I worked on my **mission statement** right after I read this.

## ORCID and Google Scholar

* [ORCID](https://orcid.org/) provides a persistent digital identifier that distinguishes you from every other researcher and, through integration in key research workflows such as manuscript and grant submission, supports automated linkages between you and your professional activities ensuring that your work is recognized.
    - It is a very good idea to register an ORCID and maintaine it from time to time.

* It is also a good idead to start a [Google scholar](https://scholar.google.com) page

## Choosing a Programing Language

* It has become clear that [`Python`](https://www.python.org/) has become the new Lingua franca in astrophysics and cosmology research and it is probably the language you want to learn first. Please check the `python` directory in `taotie` for relevant topics.
* As an advanced object-oriented programing language `C++` is still at the core of many important astrophysical applications, e.g. numerical simulations, data reduction or analysis that requires high efficiency or good performance.  Many important astrophysical softwares use `C++` as the core and then wrap it up using `Python`.
* [`Julia`](https://julialang.org/) is another intersting high-level programming language on the rising. There are [several key advantages over `Python`](https://discourse.julialang.org/t/julia-motivation-why-werent-numpy-scipy-numba-good-enough/2236) but it is still a young language.
* At the same time, `R` statistical language also has some interesting applications in astronomy; `IDL` is the language from yesterday, but for historical reasons, many projects/instruments are still using it for data reduction; `MATLAB` is also used in several occasions.
* And it never hurts if you can learn some basic programming skills related to webpage making, e.g. `HTML`, `CSS`, and `Javascript`.
* **It is also important to remember: never tool-shaming others!**. There are excellent scientists who still rely on `IDL`, `IRAF`, `Fortran`, `SuperMongo` for all kinds of reasons and they can still give us great science. Use your energy for something more positive and productive. 

## Organizing Your Research Project

* [`GitHub`](https://github.com/) or any other on line code repositories (e.g. [`GitLab`](https://about.gitlab.com/), [`bitbucket`](https://bitbucket.org/), [`coding`](https://coding.net/git)) can help organize your scientific project. It can help you do version control, back up research results, and also share results and code with the community.
    - [hub - A command-line tool that makes git easier to use with GitHub](https://github.com/github/hub)
    - You can also keep your project synced across multiple platforms. Please see [this article](https://moox.io/blog/keep-in-sync-git-repos-on-github-gitlab-bitbucket/). Notice that `gitlab` is using `v4` API now.
    - It is easy to [keeping in sync your `Git` repos on Github, Gitlab, and Bitbucket](https://moox.io/blog/keep-in-sync-git-repos-on-github-gitlab-bitbucket/). All you need to do is to make sure the repos share the same name, and add multiple remotes to the same local data.
* And `GitHub` allows you to [create new repository based on a template](https://github.blog/2019-06-06-generate-new-repositories-with-repository-templates)
    * There are template available that can help you get started:
        - [shablona - A template for small scientific python projects](https://github.com/uwescience/shablona)
* If you want to start a package as your project, you can try [`cookiecutter`](https://github.com/audreyr/cookiecutter) - A command-line utility that creates projects from templates for Python, Javascript, Ruby, Markdown, CSS, HTML etc.
    * If you are interested in using `astropy` as a good template for Python project, the [`astropy` package template](https://github.com/astropy/package-template) is available too.

## Organizing a Programming Environment

* Before starting some serious projects, you should be a little more patient on the learning curve and try to cultivate some good habbits. Good examples are everywhere!
* Don't waste too much time choosing editors or IDEs, just pick the first one you like, learn how to use it; if it does grow on you, change to another one. Both [`vim`](https://www.vim.org/) and [`emacs`](https://www.gnu.org/software/emacs/) are excellent tools; [`atom`](https://atom.io/), [`VScode`](https://code.visualstudio.com/), and [`sublime`](https://www.sublimetext.com/) are all very good IDEs. They **all** have amazing capabilities and can help you become a great coder and scientist.
* There are some useful resources that will save your time setting up the environment:
    - [`spacemacs` - A community-driven Emacs distribution](https://github.com/syl20bnr/spacemacs)
    - [`spacevim` - A community-driven modular vim distribution](https://github.com/SpaceVim/SpaceVim)
    - [Awesome Emacs - A community driven list of useful Emacs packages, libraries and others](https://github.com/emacs-tw/awesome-emacs)
    - [`neovim` - Vim-fork focused on extensibility and usability](https://github.com/neovim/neovim)
    - [`awesome-vscode` -  A curated list of delightful VS Code packages and resources](https://github.com/viatsko/awesome-vscode)
    - [`awesome-atom` - A curated list of delightful Atom packages and resources](https://github.com/mehcode/awesome-atom)

## Backing-up Your Research

* This is as important as you can possibly imagine.

* Off-line Backup:
    - You should constantly back-up your harddrive using external harddrive. Both MacOSX (e.g. [`TimeMachine`](https://support.apple.com/en-us/HT201250)) and Linux ([`TimeVault`](https://wiki.ubuntu.com/TimeVault) and [`Duplicity`](http://duplicity.nongnu.org/)) have systems that help you backup data.
    - You can also easily backup your entire system or certain directory using a command line tool [`rsync`](https://linux.die.net/man/1/rsync): `rsync -av --delete /Directory1/ /Directory2/`
        * On Linux, you can also use [`Cron`](https://opensource.com/article/17/11/how-use-cron-linux) to automatically backup files at any given time. For example, you can follow the instruction [here](https://nickjanetakis.com/blog/automatic-offline-file-backups-with-bash-and-rsync)

* Online Backup:
    - It is encouraged to use service like the [`Dropbox`](https://www.dropbox.com) to constantly backup important research-related files (e.g. draft, code, and figures). In mainland China, [`jianguoyun` (坚果云)](https://www.jianguoyun.com/) is an alternative.

## Keeping Research Notes and Documents

* [`Markdown`](https://en.wikipedia.org/wiki/Markdown) is a lightweight markup language with plain text formatting syntax. It is very easy to learn and can help you make well-organize notes and documents that can be easily converted into other format (`HTML` or `LaTeX`).
    - [Mastering Markdown by GitHub Guides](https://guides.github.com/features/mastering-markdown/) is a very good start.
    - If you want to learn more details, use [the Markdown Guide](https://www.markdownguide.org/).
    - Most of the editors and IDEs support the `.md` or `.markdown` format documents through extensions. They can help you check the syntax. There are also a lot of markdown editors on all platforms.

* Whatever notes or documents you are keeping for your research, make sure it can be backed-up and is searchable. Using software like the [`OneNote`](https://www.onenote.com/signin?wdorigin=ondc) from Microsoft, or on-line service like [`evernote`](https://evernote.com) would be a good idea.  If your project is already on `Github`, you can just use `git` to version control and back-up your documents.  [`GitHub` wiki pages](https://guides.github.com/features/wikis/) are another great way to keep notes.

## Publishing Your Science

* [A list of journals in Astronomy and Astrophysics](https://www.scimagojr.com/journalrank.php?category=3103)
    - Don't pay too much attention to the impact factor or H-index.

* Writing a paper can be painful, but it is one of the most important step in your research life. We have [a separate document talking about writing papers](https://github.com/dr-guangtou/taotie/blob/master/research/writing_paper.md).

## Sharing Your Science

* [Open Science](https://en.wikipedia.org/wiki/Open_science) is good for everybody!
* You can share your results using `Github`: you can share codes, notebooks, and draft together. But it is not very good if you have large amount of data to share.
* [zenodo - a general-purpose open-access repository developed under the European OpenAIRE program and operated by CERN](https://zenodo.org/)
* [OSF - Open Science Framework](https://osf.io/)

### Talking about Your Science

* It takes a lot of practice to know how to give a good talk, but there could be some useful tips to follow:
    - [How to give a great scientific talk by Nature](https://www.nature.com/articles/d41586-018-07780-5)
    - [Three tips for giving a great research talk by Science](https://www.sciencemag.org/careers/2019/04/three-tips-giving-great-research-talk)
    - [Speak your science by Astrobites (three parts)](https://astrobites.org/2018/02/10/speak-your-science-part-1/)

### Making a Scientific Poster

* [We're Here To Help You Make The Best Scientific Poster](https://www.makesigns.com/tutorials/)

* [Better Scientific Poster](https://osf.io/ef53g/)
    - By Mike Morrison. A new, faster approach to designing research posters. Includes templates
    - There is a [Youtube video that describes the motivation and design](https://www.youtube.com/watch?v=1RwJbhkCA58&feature=youtu.be)
    - [The LaTeX template](https://github.com/rafaelbailo/betterposter-latex-template)
    - [The R Markdown template](https://github.com/GerkeLab/betterposter)


## Reading Paper

* It is important to read as much as you can. It is important to follow `arXiv` regularly.
    - You can check if your institute is using [voxCharta](https://www.voxcharta.org), a on-line platform to vote on papers and organize `arXiv` discussion.
    - It is good idea to have a routine that keeps record of interesting papers.  Here is an examply by [me](https://github.com/dr-guangtou/daily_astroph)

* [Astrobites](https://astrobites.org) is a very good website to follow recent interesting papers from the perspective of a graduate student.
    - They also provide some good advices on reading papers: [Part I](https://astrobites.org/2017/12/19/tools-for-reading-papers-part-1/), [Part II](https://astrobites.org/2018/03/09/tools-for-reading-papers-part-2/), [Part III](https://astrobites.org/2018/09/06/tools-for-reading-papers-part-3/)

### On Using arXiv and SAO/NASA ADS

#### arXiv

- [To submit an article to arXiv](https://arxiv.org/help/submit)
    * Please read this webpage first...submitting paper to arXiv sometimes can be annoying.
- [Local time at arxiv.org](https://arxiv.org/localtime)
    * To remind you the deadline for submitting paper to arXiv
- [The official arXiv github repositories](https://github.com/arXiv)
- [arxiv.py - Python wrapper for the arXiv API](https://github.com/lukasschwab/arxiv.py)
- [arXiv LaTeX Cleaner: Easily clean the LaTeX code of your paper to submit to arXiv](https://github.com/google-research/arxiv-latex-cleaner)

#### SAO/NASA ADS

- [Tutorial for using the new ADS search](http://adsabs.github.io/help/search/)
- [Official SAO/NASA ADS github repositories](https://github.com/adsabs)
- [ads - A Python Module to Interact with NASA's ADS that Doesn't Suck](https://github.com/andycasey/ads)

## Communicating with Others

* [`Slack`](https://slack.com/) has become the most common way to organize a small collaboration.  Even the free version can be very useful.
* Telecon becomes more and more frequently used to communicate among collaborators in different institutes and timezones.  Commonly used telecon tools including [`Skype`](https://www.skype.com/en/), [`zoom`](https://zoom.us/), [`GoToMeetings`](https://www.gotomeeting.com/)
    - All of these tools are free and cross-platform, and easy to use. You can share screen using them for remote presentation too.
* [Doodle](https://doodle.com/make-a-poll) is the most commonly used tool to create a poll to decide the time slot for a meeting or telecon.

### Personal Website

* It is actually pretty important to have a visible personal website that links your CV and contact information.  Make sure that it can be found by search engine.
* This is especially important if you try to find job in another country (e.g. get a PhD in China, want a post-doc job in Europe) or when you know the hiring committee is not familiar with you.

* [`GitHub Pages`](https://pages.github.com/) is pretty good choice to make a nice-looking personal website.  And there are some [easy-to-use templates available](https://pages.github.com/themes/), and there are [more fancy ones available](https://jekyllthemes.io/github-pages-templates)
    - [How to Create a Simple Academic Website](https://marisacarlos.com/pages/create-simple-academic-website)

* [al-folio - A beautiful Jekyll theme for academics](https://github.com/alshedivat/al-folio)
    * This is a pretty good template for academic personal wesbsite

* Good examples (personal choice: clean and informative)
    - [Adrian Price-Whelan](http://adrian.pw/); the code can be found [here](https://github.com/adrn/adrn.github.io)
    - [Dan Foreman-Mackey](https://dfm.io/); the code can be found [here](https://github.com/dfm/dfm.io)

### Scientific Conference

* [CADA International Astronomy Meetings](http://www.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/en/meetings/) is a very good place to check if there is anything conference that interests you in the future. There is a RSS Feed and a `iCal` subscription.
* [@astromeetings Twitter account](https://twitter.com/astromeetings?lang=en) is also a good way to follow the on-going conferences in your field.
    - It has become routine for a conferece to have a designated hashtag on Twitter for people to twit about the talk.  We cannot go to all conferences (and it is [bad for the mother earth](https://onlinelibrary.wiley.com/doi/pdf/10.1111/1746-692X.12106))
* [Future IAU Meetings](https://www.iau.org/science/meetings/future/)

## Keep Learning

### On-line Colloquium

* With Youtube, it is pretty easy to enjoy great astrophysical colloquium in universities and institutes all over the world.  Here are a few good channels to get started:
    - [CfA Colloquium](https://www.youtube.com/channel/UCApHNlZLkxmiV95A0ChueYg) and [ITC Video](https://www.youtube.com/channel/UCTuACIrLKPTlp6XMZbeipig/featured) from Harvard/CfA
    - [Heidelberg Astronomy](https://www.youtube.com/user/AstronomyHeidelberg)
    - [CCA Seminars](https://www.youtube.com/user/SimonsFoundation/playlists). Some of them are about astronomy and cosmology.
    - [Dept of Physics & Astronomy at the University of Utah](https://www.youtube.com/user/UofUPhysAstro/featured)