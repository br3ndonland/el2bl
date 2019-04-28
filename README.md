# el2bl

Convert [Evernote](https://evernote.com/) internal relative note links to [Bear](https://bear.app/) note links

<img src="img/evernote-logo.png" alt="Evernote logo" height="100px" /><img src="img/baseline-arrow_forward-24px.svg" alt="Right arrow" height="100px" /><img src="img/python-logo.svg" alt="Python logo" height="100px" /><img src="img/baseline-arrow_forward-24px.svg" alt="Right arrow" height="100px" /><img src="img/bear-logo.png" alt="Bear logo" height="100px" />

## Table of Contents <!-- omit in toc -->

- [Introduction](#introduction)
  - [The externalized mind](#the-externalized-mind)
  - [The Evernote entrypoint](#the-evernote-entrypoint)
  - [The Joplin jam](#the-joplin-jam)
  - [The Bear buoyance](#the-bear-buoyance)
- [Development environment](#development-environment)
  - [Text Editor](#text-editor)
  - [Git](#git)
  - [Markdown](#markdown)
  - [Python](#python)
- [Development process](#development-process)
  - [Locating files](#locating-files)
  - [Opening files](#opening-files)
  - [Matching patterns](#matching-patterns)
  - [Parsing Evernote exports with Beautiful Soup](#parsing-evernote-exports-with-beautiful-soup)
  - [Saving files](#saving-files)

## Introduction

### The externalized mind

> What one ought to learn is how to extract patterns! You don't bother to memorize the literature-you learn to read and keep a shelf of books. You don't memorize log and sine tables; you buy a slide rule or learn to punch a public computer! … You don't have to know everything. You simply need to know where to find it when necessary.

From _Stand on Zanzibar_ by John Brunner, Continuity 3

In the prescient 1968 science fiction novel _Stand on Zanzibar_, author John Brunner envisioned the coming Information Age. Brunner realized that the keys to success would be externalizing and finding information.

There is simply too much information for us to remember in biological memory (our brains), so we write it down and externalize it. In the past, paper books were the medium of choice, and today, we delegate the storage of information to computing machines. We use computer memory to store information, and operating systems to interact with memory.

We also need search engines to find information stored in computer memory. Search engines have become particularly important on the World Wide Web. The early days of the World Wide Web featured search engines with page results manually curated and organized by humans, but it became impossible for humans to organize that much information. Humans wrote algorithms (computer instructions), such as Google's PageRank, to organize information more efficiently, and search engines to locate the organized information for users. Google's [stated mission](https://www.google.com/about/) is to "organize the world's information and make it universally accessible and useful." We all use search engines on the internet now.

Internet search engines can't do everything though. Note apps enable users to create searchable personal knowledgebases. Entering information into a note app creates an externalized mind, where information is retained and rapidly searched, and where disparate information sources can be connected in new ways. Clipping articles into a note app removes ads and formatting, stores the articles to read later, and helps assess sources of information over time. This is becoming more and more important, because we're presented with feeds that are manipulated by [BUMMER](https://www.amazon.com/dp/B07CX579TC) algorithms.

### The Evernote entrypoint

Back in 2011, Evernote helped me digitize the information in my life and start externalizing my mind. By 2019, after eight years of extensive use, I had 5500 notes that formed a valuable personal knowledgebase. I had also experienced many bugs and frustrations over those eight years, and wanted to switch to a new note app.

I definitely knew I wanted to ditch the Evernote XML format (sort of HTML-in-XML) and switch to Markdown. There are many note apps that use Markdown now, so it wasn't an issue. For some Markdown note app options, check out [Notable's comparison chart](https://raw.githubusercontent.com/notable/notable/master/resources/comparison/table.png) and [my Markdown guide](https://github.com/br3ndonland/udacity-fsnd/blob/master/info/markdown-guide.md).

Another key feature I was looking for was note linking. Note links lead from one note to another within Evernote. Each note has its own link. Over time, note links create a personal encyclopedia or mind map of the connections among your notes, and enable quick navigation within the app. I therefore wanted to preserve the many note links I had created over the years. However, all the note apps I tried shared the same problem: Evernote note links aren't converted on import.

I first attempted to switch to Joplin, but settled on Bear because of how it handles note links.

### The Joplin jam

I tried out Joplin, but found that internal note links import as Evernote links, not Joplin links. This is a critical issue for me. Links sometimes also just lead to the top note result in the notebook, rather than the specific note needed. To investigate this, I filed GitHub issue #[585](https://github.com/laurent22/joplin/issues/585). The developer, Laurent Cozic, didn't even know you could make internal note links. Not a good sign. Laurent [closed the issue](https://github.com/laurent22/joplin/issues/585#issuecomment-418166252) because "Evernote doesn't export the note IDs."

The [Evernote Developer API article on note links](https://dev.evernote.com/doc/articles/note_links.php) explains that relative links contain the note GUID. However, the .enex export doesn't attach the note GUID to the notes, so it's only possible for the Evernote source code (which is not open-source) to connect the GUID with the correct note.

### The Bear buoyance

One of the best Markdown note apps I came across was [Bear](https://bear.app/). I was happy with the features and user experience overall, but it still failed to convert Evernote note links into Bear note links. I decided to reach out to Bear support to see if there was any way I could use it. Here's a support ticket I sent to Bear 20190301 (received by Bear Sat, Mar 2, 2019 at 02:10 AM):

> I have been a heavy Evernote user for eight years. I've never been happy with it, and would love to switch to Bear. My main problem is note links (pointing to another note within Evernote). The note links are extremely important for me because they create a sort of mind map or personal Wikipedia that allows me to connect all my information. I have many internal/relative note links, and when imported into Bear, the links remain pointed at Evernote instead of Bear notes. The links look like this:
>
> `evernote:///view/6168869/s55/a51fb62f-8696-46ec-88d1-cceb38b2a2ed/a51fb62f-8696-46ec-88d1-cceb38b2a2ed/`
>
> The "s55" might point to a database shard, and then I guess there's some sort of note ID after that. This is probably something Evernote handles on the back-end, and there might not be any way to know what the links actually point to in an exported .enex file.
>
> The [Evernote Developer API article on note links](https://dev.evernote.com/doc/articles/note_links.php) explains that relative links contain the note GUID. However, the .enex export doesn't include the GUIDs with the notes.
>
> I attached a .enex file containing two notes with relative links in case this helps. I had used it to test import into another note app, Joplin. See [Joplin issue #585](https://github.com/laurent22/joplin/issues/585) for a similar discussion.
>
> Is there anything I can do? I probably have tens of thousands of these links in my 5500 notes, and it's just not feasible to correct the links after import into Bear. If I could figure out how to output the GUID, I could add it to each note's metadata and write a script to convert it to Joplin. I'm a developer and would be happy to run a script over the .enex prior to import if that helps.
>
> Thanks for your help, and keep up the good work.

Here's the response:

> Hi Brendon
>
> Thank you for reaching us out.
>
> Unfortunately, these links will not be converted into the bear note links due to different workflow and separate API that Bear and Evernote use. Please refer to this link for the notes linking in the Bear app https://bear.app/faq/Tags%20&%20Linking/How%20to%20link%20notes%20together/
>
> Please let us know if you have any more concerns/questions.
>
> Thank you.

I wasn't deterred by this response. After working with Bear a bit more, I was buoyed when I realized it has a key feature: [creating note links](https://bear.app/faq/Tags%20&%20Linking/How%20to%20link%20notes%20together/) by placing note titles within double brackets, like `[[Note title]]`. Much as the Evernote source code matches up note GUIDs with the correct notes, the Bear source code locates the note using the title within the double brackets, and links the note appropriately.

This means that you can't change note titles after import. If note titles are changed, Bear won't be able to locate the notes. Clicking a note link after the title has been changed will create an empty note (as of version 1.6.13 (7111) for macOS). The inability to change note titles is is a small price to pay for retaining note links though.

I decided to write a Python script that would convert Evernote note links to Bear note links.

## Development environment

### Text Editor

- The code in this repository was written with [Microsoft Visual Studio Code](https://code.visualstudio.com/) (VSCode).
- My full VSCode config is available in [this public GitHub Gist](https://gist.github.com/br3ndonland/01b625629ef98ec7a919a7b927d0ddaf). If you would like to use these settings, you can fork the gist into your account, and pull in the settings with the [Settings Sync extension](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync).

### Git

- Code was version-controlled with [Git](https://www.git-scm.com/), using the following general Git practices:
  - Imperative, capitalized commit title limited to 50 characters and without a period at the end
  - Blank line between commit title and body
  - Commit body wrapped at 72 characters
  - When branching:
    - The `master` and `develop` branches are generally long-running branches.
    - Short-lived feature branches are merged to `develop`, then deleted.
    - The only commits to `master` are production-ready merges from `develop`.
- Here's a sample commit message based on the practices above:

  ```text
  Imperative commit title limited to 50 characters
  # Blank line
  - More detailed commit message body
  - List of key points and updates that the commit provides
  - Lines need to be manually wrapped at 72 characters
  ```

- Git pre-commit hooks are managed with [pre-commit](https://pre-commit.com/). After cloning the repository, enter the Python virtual environment and install pre-commit:

  ```sh
  pipenv shell
    pre-commit install
  ```

### Markdown

- Markdown was written with the [Markdown All in One VSCode extension](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one), and autoformatted with [Prettier](https://prettier.io/) using the [Prettier VSCode extension](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode).
  - The [Prettier pre-commit hook](https://prettier.io/docs/en/precommit.html) was installed.

### Python

#### Pipenv

- **[Pipenv](https://pipenv.readthedocs.io/en/latest/)** was used to manage the development virtual environment for this project.

  - Install Pipenv with a system package manager like [Homebrew](https://brew.sh/), or with the Python package manager `pip`.
  - Use Pipenv to install the virtual environment from the Pipfile with `pipenv install --dev`. The `dev` flag was used to accommodate the Black autoformatter (see [code style](#code-style) below).

    ```sh
    cd path/to/repo
    pipenv install --dev
    ```

  - Activate the virtual environment with `pipenv shell`.
  - When generating a _Pipfile.lock_ containing dev packages, add the `--pre` flag to allow pre-releases into the lock file: `pipenv lock --pre`.

- VSCode can be configured to recognize the Pipenv virtual environment. See [Using Python environments in VS Code](https://code.visualstudio.com/docs/python/environments).
  - _Command Palette -> Python: Select Interpreter_. Select virtual environment.
  - _Command Palette -> Python: Create Terminal_. Creates a terminal and automatically activates the virtual environment. If the virtual environment is set as the interpreter for the workspace, new terminal windows will automatically start in the virtual environment.

#### Code style

- Python code was autoformatted with [Black](https://black.readthedocs.io/en/stable/).
  - Black limits line length to 88 characters.
  - Black is still considered a pre-release. As described in [Pipenv](#pipenv), pre-releases must be installed with the `--dev` flag (`pipenv install black --dev`), then added to the _Pipfile.lock_ with the `--pre` flag (`pipenv lock --pre`).
  - The [Black Git pre-commit hook](https://black.readthedocs.io/en/stable/version_control_integration.html) has been installed for this project.

## Development process

### Locating files

- The first step is to locate a set of Evernote export files.
- Verifying the file path: `os.path`

### Opening files

#### fileinput

- Brian Okken wrote a [blog post](https://pythontesting.net/python/regex-search-replace-examples/) about using `fileinput` for find and replace, back in 2013. I considered `fileinput` after reading his post, but didn't particularly like it.
- `fileinput` is annoying to use and doesn't have strong community support, as this StackOverflow user [says](https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file-using-python#comment43539292_20593644):
  > If you really want to redirect stdout to your file for some reason, it's not hard to do it better than fileinput does (basically, use try..finally or a contextmanager to ensure you set stdout back to it's original value afterwards). The source code for fileinput is pretty eye-bleedingly awful, and it does some really unsafe things under the hood. If it were written today I very much doubt it would have made it into the stdlib. – craigds Dec 18 '14 at 22:06

#### Opening files and the `with` statement

- The [`with` statement](https://docs.python.org/3/reference/compound_stmts.html#with) was introduced in [PEP 343](https://www.python.org/dev/peps/pep-0343/).
- As explained in the [Python Tricks context managers article](https://dbader.org/blog/python-context-managers-and-with-statement) and the [Python Tricks file i/o article](https://dbader.org/blog/python-file-io), the advantage of using the `with` statement over simply `file.open()` is that it creates a context under which file operations can occur and be automatically concluded.

### Matching patterns

#### Regular expressions

- After opening a file, Evernote links can be located with regular expressions (regex).
- [RegExr](https://regexr.com/) can be used to test out regex.

#### re

- The Python [`re`](https://docs.python.org/3/library/re.html) package provides helpful features for regex operations.
- Raw string notation (`r""`) enables developers to enter regular expressions into Python code without having to escape special characters, as described in the [`re` documentation](https://docs.python.org/3/library/re.html#raw-string-notation).
- An Evernote note link can be matched with `re.compile(r'(<a href="evernote.*?>)(.*)(</a>)')`

#### Pampy

- I also tried another pattern matching package, Pampy (Pattern Matching for Python, [GitHub](https://github.com/santinic/pampy) | [PyPI](https://pypi.org/project/pampy/)). Pampy helps flexibly match patterns and make code more readable. There are some use cases for which Pampy could be quite helpful (for example, matching dictionaries and tuples).
- I heard about Pampy on [Python Bytes episode 107](https://pythonbytes.fm/episodes/show/107/restructuring-and-searching-data-the-python-way) (December 7, 2018).
- I wrote up a preliminary function to match links in a _.enex_ Evernote export file:

  ```py
  def match_link(file):
      """Match link in .enex file with Pampy:
      Open file
      Match based on regular expression with re.compile()
      Use lambda function to print link title
      """
      try:
          path = input("Please provide the file path to your Evernote exports: ")
          if os.path.exists(path):
              print(f"{path} is a valid file path.")
              if not os.path.exists(f"{path}/bear"):
                  os.mkdir(f"{path}/bear")
              files = os.scandir(path)
              print("List of files:")
              for file in files:
                  if file.name.endswith(".enex") and file.is_file():
                      print(f"Evernote export file name: {file.name}")
                      enex = open(file).read()
                      return match(
                          enex,
                          re.compile(r'(<a href="evernote.*?>)(.*)(</a>)'),
                          lambda link_start, title, link_end: print(f"Link title: {title}"),
                      )
          else:
              print(f"{path} is not a valid path.")
      except Exception as e:
          print(f"An error occurred:\n{e}\nPlease try again.")

  ```

- After working with Pampy, I didn't find that it addressed my needs in this project. Finding all matches, replacing matches, and working with strings were not as easy as they should be.

### Parsing Evernote exports with Beautiful Soup

- I decided to try out [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/). There are a few other options described in [The Hitchhiker's Guide to Python scenario guide to XML parsing](https://docs.python-guide.org/scenarios/xml/), which strangely does not mention Beautiful Soup.
- [Selecting a parser](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser):
  - This is not straightforward, because Evernote XML is a blend of XML and HTML.
  - I first tried [parsing XML](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#parsing-xml), using `xml`, the XML parser in `lxml`. I couldn't match links, and HTML elements were being read like `&lt;div&gt;` instead of `<div>`.
  - Notes didn't parse as expected when opening as HTML with `html.parser`.
  - I ended up using `lxml` (the HTML parser in `lxml`). It was lenient enough to skip over the XML parts and correctly parse the HTML.
- Now that I had a parser, I had to match Evernote note links.

  - I started by learning about the different [kinds of filters](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#kinds-of-filters).
  - I used an `href` attribute filter and a regular expression filter to identify Evernote note links. This method avoids replacing URLs that are not Evernote note links, such as https://evernote.com/, and Evernote note links outside of anchor tags, such as the text "the links are converted to `evernote:///`." The function looked like this:

    ```py
    def note_link(href):
        """Identify note link URIs using href attribute and regex"""
        return href and re.compile(r"evernote://").search(href)
    ```

  - I then passed the `note_link()` function into [`soup.find_all()`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all) to locate all note links, extracted the strings (note titles) from the links using the [string argument](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#the-string-argument), and replaced the links with the titles within double brackets.

    ```py
    for link in soup.find_all(href=note_link):
        string = link.string.extract()
        bear_link = link.replace_with(f"[[{string}]]")
    ```

### Saving files

- The last step was to save the Beautiful Soup object to a new file.
