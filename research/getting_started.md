# Getting Started as Researcher


## Choosing a Programing Language

* It has become clear that [`Python`](https://www.python.org/) has become the new Lingua franca in astrophysics and cosmology research and it is probably the language you want to learn first. Please check the `python` directory in `taotie` for relevant topics.
* As an advanced object-oriented programing language `C++` is still at the core of many important astrophysical applications, e.g. numerical simulations, data reduction or analysis that requires high efficiency or good performance.  Many important astrophysical softwares use `C++` as the core and then wrap it up using `Python`. 
* [`Julia`](https://julialang.org/) is another intersting high-level programming language on the rising. There are [several key advantages over `Python`](https://discourse.julialang.org/t/julia-motivation-why-werent-numpy-scipy-numba-good-enough/2236) but it is still a young language. 
* At the same time, `R` statistical language also has some interesting applications in astronomy; `IDL` is the language from yesterday, but for historical reasons, many projects/instruments are still using it for data reduction; `MATLAB` is also used in several occasions.
* And it never hurts if you can learn some basic programming skills related to webpage making, e.g. `HTML`, `CSS`, and `Javascript`.

## Organize Project

* [`GitHub`](https://github.com/) or any other on line code repositories (e.g. [`GitLab`](https://about.gitlab.com/), [`bitbucket`](https://bitbucket.org/), [`coding`](https://coding.net/git)) can help organize your scientific project. It can help you do version control, back up research results, and also share results and code with the community.
* There are template available that can help you get started:
    - [shablona - A template for small scientific python projects](https://github.com/uwescience/shablona)
* And `GitHub` allows you to [create new repository based on a template](https://github.blog/2019-06-06-generate-new-repositories-with-repository-templates)

## ORCID and Google Scholar

* [ORCID](https://orcid.org/) provides a persistent digital identifier that distinguishes you from every other researcher and, through integration in key research workflows such as manuscript and grant submission, supports automated linkages between you and your professional activities ensuring that your work is recognized.
    - It is a very good idea to register an ORCID and maintaine it from time to time.

* It is also a good idead to start a [Google scholar](https://scholar.google.com) page 

## Backup Research Project

* This is as important as you can possibly imagine.
    - You should constantly back-up your harddrive using external harddrive. Both MacOSX and Linux have systems that help you backup data.
    - It is encouraged to use service like the [`Dropbox`](https://www.dropbox.com) to constantly backup important research-related files (e.g. draft, code, and figures). In mainland China, [`jianguoyun` (坚果云)](https://www.jianguoyun.com/) is an alternative.

## Reading Paper

* It is important to read as much as you can. It is important to follow `arXiv` regularly.
    - You can check if your institute is using [voxCharta](https://www.voxcharta.org), a on-line platform to vote on papers and organize `arXiv` discussion.
    - It is good idea to have a routine that keeps record of interesting papers.  Here is an examply by [me](https://github.com/dr-guangtou/daily_astroph)

* [Astrobites](https://astrobites.org) is a very good website to follow recent interesting papers from the perspective of a graduate student.
    - They also provide some good advices on reading papers: [Part I](https://astrobites.org/2017/12/19/tools-for-reading-papers-part-1/), [Part II](https://astrobites.org/2018/03/09/tools-for-reading-papers-part-2/), [Part III](https://astrobites.org/2018/09/06/tools-for-reading-papers-part-3/)

### On using arXiv and SAO/NASA ADS

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

## Communication

* [`Slack`](https://slack.com/) has become the most common way to organize a small collaboration.  Even the free version can be very useful.
* Telecon becomes more and more frequently used to communicate among collaborators in different institutes and timezones.  Commonly used telecon tools including [`Skype`](https://www.skype.com/en/), [`zoom`](https://zoom.us/), [`GoToMeetings`](https://www.gotomeeting.com/)
    - All of these tools are free and cross-platform, and easy to use. You can share screen using them for remote presentation too.
* [Doodle](https://doodle.com/make-a-poll) is the most commonly used tool to create a poll to decide the time slot for a meeting or telecon.

## Personal Website

* It is actually pretty important to have a visible personal website that links your CV and contact information.  Make sure that it can be found by search engine.
* This is especially important if you try to find job in another country (e.g. get a PhD in China, want a post-doc job in Europe) or when you know the hiring committee is not familiar with you.

* [`GitHub Pages`](https://pages.github.com/) is pretty good choice to make a nice-looking personal website.  And there are some [easy-to-use templates available](https://pages.github.com/themes/), and there are [more fancy ones available](https://jekyllthemes.io/github-pages-templates)
    - [How to Create a Simple Academic Website](https://marisacarlos.com/pages/create-simple-academic-website)

* [al-folio - A beautiful Jekyll theme for academics](https://github.com/alshedivat/al-folio)
    * This is a pretty good template for academic personal wesbsite

* Good examples (personal choice: clean and informative)
    - [Adrian Price-Whelan](http://adrian.pw/); the code can be found [here](https://github.com/adrn/adrn.github.io)
    - [Dan Foreman-Mackey](https://dfm.io/); the code can be found [here](https://github.com/dfm/dfm.io)

## Scientific Conference

* [CADA International Astronomy Meetings](http://www.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/en/meetings/) is a very good place to check if there is anything conference that interests you in the future. There is a RSS Feed and a `iCal` subscription.
* [@astromeetings Twitter account](https://twitter.com/astromeetings?lang=en) is also a good way to follow the on-going conferences in your field.
    - It has become routine for a conferece to have a designated hashtag on Twitter for people to twit about the talk.  We cannot go to all conferences (and it is [bad for the mother earth](https://onlinelibrary.wiley.com/doi/pdf/10.1111/1746-692X.12106))
* [Future IAU Meetings](https://www.iau.org/science/meetings/future/)

## Giving a talk

* It takes a lot of practice to know how to give a good talk, but there could be some useful tips to follow:
    - [How to give a great scientific talk by Nature](https://www.nature.com/articles/d41586-018-07780-5)
    - [Three tips for giving a great research talk by Science](https://www.sciencemag.org/careers/2019/04/three-tips-giving-great-research-talk)
    - [Speak your science by Astrobites (three parts)](https://astrobites.org/2018/02/10/speak-your-science-part-1/)

## Making a poster

* [We're Here To Help You Make The Best Scientific Poster](https://www.makesigns.com/tutorials/)

## Colloquium

* With Youtube, it is pretty easy to enjoy great astrophysical colloquium in universities and institutes all over the world.  Here are a few good channels to get started:
    - [CfA Colloquium](https://www.youtube.com/channel/UCApHNlZLkxmiV95A0ChueYg) and [ITC Video](https://www.youtube.com/channel/UCTuACIrLKPTlp6XMZbeipig/featured) from Harvard/CfA
    - [Heidelberg Astronomy](https://www.youtube.com/user/AstronomyHeidelberg)
    - [CCA Seminars](https://www.youtube.com/user/SimonsFoundation/playlists). Some of them are about astronomy and cosmology.
    - [Dept of Physics & Astronomy at the University of Utah](https://www.youtube.com/user/UofUPhysAstro/featured)