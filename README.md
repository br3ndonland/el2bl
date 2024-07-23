# el2bl

Migrate your notes from [Evernote](https://evernote.com/) to [Bear](https://bear.app/), retaining note links

<img src="img/evernote-logo.png" alt="Evernote logo" height="100px" /><img src="img/baseline-arrow_forward-24px.svg" alt="Right arrow" height="100px" /><img src="img/python-logo.svg" alt="Python logo" height="100px" /><img src="img/baseline-arrow_forward-24px.svg" alt="Right arrow" height="100px" /><img src="img/bear-logo.png" alt="Bear logo" height="100px" />

## Table of Contents <!-- omit in toc -->

- [Quickstart](#quickstart)
- [Overview](#overview)
  - [The externalized mind](#the-externalized-mind)
  - [The Evernote entrypoint](#the-evernote-entrypoint)
  - [The Joplin jilt](#the-joplin-jilt)
  - [The Bear buoyance](#the-bear-buoyance)
- [Scripting](#scripting)
  - [Reading and writing files](#reading-and-writing-files)
  - [Parsing Evernote exports](#parsing-evernote-exports)
  - [Matching patterns](#matching-patterns)

## Quickstart

```sh
git clone git@github.com:br3ndonland/el2bl.git
cd el2bl
python el2bl.py
```

```text
Please input the path to a directory with Evernote exports: tests
Converting export.enex...
Converted export.enex. New file available at tests/bear/export.enex.
```

## Overview

### The externalized mind

> What one ought to learn is how to extract patterns! You don't bother to memorize the literature-you learn to read and keep a shelf of books. You don't memorize log and sine tables; you buy a slide rule or learn to punch a public computer!
> ...
> You don't have to know everything. You simply need to know where to find it when necessary.[^1]

In the prescient 1968 science fiction novel _Stand on Zanzibar_, author John Brunner envisioned the coming Information Age. Brunner realized that the keys to success would be externalizing and finding information.

There is simply too much information for us to remember in biological memory (our brains), so we write it down and externalize it. In the past, paper books were the medium of choice, and today, we delegate the storage of information to computing machines. We use computer memory to store information, and operating systems to interact with memory.

We also need search engines to find information stored in computer memory. Search engines have become particularly important on the World Wide Web. The early days of the World Wide Web featured search engines with page results manually curated and organized by humans, but it became impossible for humans to organize that much information. Humans wrote algorithms (computer instructions), such as Google's PageRank, to organize information more efficiently, and search engines to locate the organized information for users. Google's stated mission was to "organize the world's information and make it universally accessible and useful." We all use search engines on the World Wide Web now.

It's not always efficient or practical to search the entire World Wide Web for every single query. Instead of relying only on web search, it helps to store smaller amounts of information in notes. Notes apps enable users to collect and connect their notes, creating a <a href="https://en.wikipedia.org/wiki/Personal_information_management" rel="external" target="_blank">personal information management</a> system or "externalized mind." Information is retained and rapidly searched, and disparate information sources can be connected in new ways. Clipping articles into a notes app removes ads and formatting, stores the articles to read later, and helps readers assess sources over time. This is becoming more and more important, because we're presented with feeds that are manipulated by <a href="https://www.jaronlanier.com/tenarguments.html" rel="external" target="_blank">BUMMER</a> algorithms.

### The Evernote entrypoint

Back in 2011, <a href="https://evernote.com/" rel="external" target="_blank">Evernote</a> helped me digitize the information in my life and start externalizing my mind. By 2019, after eight years of extensive use, I had 5500 notes that formed a valuable personal knowledge base. I had also experienced many bugs and frustrations over those eight years, and wanted to switch to a new notes app.

I wanted to ditch the <a href="https://web.archive.org/web/20240513142647/https://evernote.com/blog/how-evernotes-xml-export-format-works" rel="external" target="_blank">Evernote XML format</a> (sort of HTML-in-XML) and switch to a new notes app that supported <a href="https://www.markdownguide.org/" rel="external" target="_blank">Markdown</a>, a plain-text format based on <a href="https://developer.mozilla.org/en-US/docs/Web/HTML" rel="external" target="_blank">HTML</a>, the language used to structure web pages. There are <a href="https://www.markdownguide.org/tools/" rel="external" target="_blank">many notes apps that support Markdown</a>.

Another key feature I was looking for was <a href="https://web.archive.org/web/20240531045315/https://bear.app/faq/how-to-link-notes-together/" rel="external" target="_blank">note links</a>, also sometimes called "backlinks," "internal links," "Wiki Links" or "WikiLinks." Note links lead from one note to another within the app. Over time, note links create a mind map of the connections among your notes, and enable quick navigation within the app. I therefore wanted to preserve the many note links I had created over the years.

In plain-text, Evernote note links look like this:

```html
<a
  style="color: rgb(105, 170, 53);"
  href="evernote:///view/6168869/s55/ef6f76d8-5804-486c-9259-43e80a1b0ff9/ef6f76d8-5804-486c-9259-43e80a1b0ff9/"
  >Title</a
>
```

**All the notes apps I tried shared the same problem: Evernote note links weren't converted on import**.

### The Joplin jilt

I tried an app called Joplin. When importing my notes, note links were not converted from Evernote format to Joplin format. This was a deal-breaker for me. I asked about this <a href="https://github.com/laurent22/joplin/issues/585" rel="external" target="_blank">on GitHub</a>. The developer didn't even know about note links, and closed the issue because "Evernote doesn't export the note IDs."

The <a href="https://web.archive.org/web/20240521001122/https://dev.evernote.com/doc/articles/note_links.php" rel="external" target="_blank">Evernote Developer API article on note links</a> explains that relative links contain the note GUID. However, the `.enex` export doesn't attach the note GUID to the notes, so it's only possible to connect the GUID with the correct note within Evernote itself.

### The Bear buoyance

One of the best apps I came across was <a href="https://bear.app/" rel="external" target="_blank">Bear</a>. I was happy with the features and user experience overall, but it still failed to convert Evernote note links into Bear note links. I reached out to Bear support about this. Support responded by saying Bear could not convert Evernote note links "due to different workflow and separate API that Bear and Evernote use." Pretty lame, but I wasn't deterred by this response.

After working with Bear a bit more, I was buoyed when I realized it has a key feature: <a href="https://web.archive.org/web/20240531045315/https://bear.app/faq/how-to-link-notes-together/" rel="external" target="_blank">note links</a>, created by placing note titles within double brackets, like `[[Title]]`. Much as the Evernote source code matches up note GUIDs with the correct notes, the Bear source code locates the note using the title within double brackets, and links the note appropriately. This means that changing note titles could break the links. As of Bear 1.7, this isn't a problem, because Bear automatically updates note links when note titles change.

I decided to write a script that would convert note links from Evernote format to Bear format. I chose Python for this project, but for a comparable JavaScript/TypeScript implementation, see <a href="https://github.com/notable/dumper" rel="external" target="_blank">notable/dumper</a>.

## Scripting

### Reading and writing files

I used the `os` module for working with file paths. File paths can be verified with `os.path.exists()`. Directories can be created with `os.mkdir()`.

I used `with` context managers to work with file contents. The <a href="https://docs.python.org/3/reference/compound_stmts.html#with" rel="external" target="_blank">`with` statement</a> was introduced in <a href="https://www.python.org/dev/peps/pep-0343/" rel="external" target="_blank">PEP 343</a>, and provides context management for working with files. Within a `with` context, file operations can occur and be automatically concluded. To save output to a new file, I used a `with` statement, and included `"x"` for exclusive creation mode, which creates the new file. I also looked into <a href="https://docs.python.org/3/library/fileinput.html" rel="external" target="_blank"><code>fileinput</code></a>, but decided against it because it didn't add much value beyond a simple `with` context.

### Parsing Evernote exports

I decided to try out <a href="https://www.crummy.com/software/BeautifulSoup/" rel="external" target="_blank">Beautiful Soup</a>. Beautiful Soup is usually used to parse webpages, but Evernote notes are somewhat like webpages, so it could work.

<a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser" rel="external" target="_blank">Selecting a parser</a> was not straightforward. Evernote XML is a blend of XML and HTML, and many parsers depend on a valid HTML document.

I first tried `xml`, the XML parser in `lxml`. I couldn't match links, and HTML elements were being read like `&lt;div&gt;` instead of `<div>`.

I had some success with the HTML parser in `lxml`. It was lenient enough to read the XML parts, and parse the document into valid HTML. The `lxml` parser made it easy to match Evernote note links:

1. I started by learning about the different <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/#kinds-of-filters" rel="external" target="_blank">kinds of filters</a>.
2. I used an `href` attribute filter and a regular expression filter to identify Evernote note links. This method avoided replacing URLs that were not Evernote note links. The function looked like this:

   ```py
   def note_link(href):
       """Identify note link URIs using href attribute and regex"""
       return href and re.compile(r"evernote://").search(href)
   ```

3. I then passed the `note_link()` function into <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all" rel="external" target="_blank">`soup.find_all()`</a> to locate all note links, extracted the strings (note titles) from the links using the <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/#the-string-argument" rel="external" target="_blank">string argument</a>, and replaced the links with the titles within double brackets.

   ```py
   for link in soup.find_all(href=note_link):
       string = link.string.extract()
       bear_link = link.replace_with(f"[[{string}]]")
   ```

4. I could then print the output and see the note links properly replaced within the notes. The full function looked like this:

   ```py
   def convert_links(file):
       """Convert links in .enex files to Bear note link format.
       """
       with open(file) as enex:

           def note_link(href):
               """Identify note link URIs using href attribute and regex"""
               return href and re.compile(r"evernote://").search(href)

           soup = BeautifulSoup(enex, "lxml")
           for link in soup.find_all(href=note_link):
               string = link.string.extract()
               bear_link = link.replace_with(f"[[{string}]]")
           with open(f"{os.path.dirname(file)}/bear/{file.name}", "x") as new_enex:
               new_enex.write(str(soup))
   ```

The problem was that, in order to parse the document, `lxml` was adding `<html>` and `<body>` tags and removing the `CDATA` sections. Trying to import files modified in this way crashed Bear. I had similar problems with `html5lib`. The html5lib parser also forces some formatting by adding comments around the XML portions.

I then went back to the default Python `html.parser`. The `html.parser` doesn't modify formatting, but because the Evernote export is not valid HTML, it's not able to parse the tags like `lxml` does.

The note body was located within the `content` tag. I considered selectively parsing the `content` tag with <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/#parsing-only-part-of-a-document" rel="external" target="_blank">SoupStrainer</a>.

At this point, I realized I could rely on `re` to match and replace regular expressions in the entire document, rather than trying to get Beautiful Soup to identify specific links.

### Matching patterns

#### Regular expressions and `re`

The Python <a href="https://docs.python.org/3/library/re.html" rel="external" target="_blank"><code>re</code></a> package provides helpful features for regular expression ("regex") operations. It supports raw string notation (`r""`) so that regular expressions can be written in Python code without having to escape special characters.

Initially, I matched Evernote note links with `re.compile(r'(<a href="evernote.*?>)(.*?)(</a>?)')` and replaced them with `re.sub(r'(<a href="evernote.*?>)(.*?)(</a>?)', r"[[\2]]", soup)`. The `\2` was a backreference to the second capture group (the string inside the note link), which was the note title. The question mark was particularly important in the second capture group, `(.*?)`. Without the question mark, Python will continue through the remainder of the string to the last occurrence of the third capture group `(</a>?)`, rather than stopping at the first occurrence.

I used a second regular expression to strip H1 tags out of the notes. Many of my clipped news articles included the article title within `<h1>` HTML tags. In Bear, the note title itself serves as H1, so the additional H1 within the note was unnecessary. I could have completely deleted these H1 elements, but I decided to retain just the text in case I had made changes from the original article titles. Again here, I used a backreference to the second capture group to retain the text within the H1 tags. To run both the `re.sub()` operations, I just overwrote the object created from the first `re.sub()`.

```py
soup_sub = re.sub(r'(<a href="evernote.*?>)(.*?)(</a>?)', r"[[\2]]", soup)
soup_sub = re.sub(r"(<h1>?)(.*?)(</h1>?)", r"\2", soup_sub)
```

I then wrote the `soup_sub` object to a new file using a `with` context again.

```py
with open(file) as enex:
    soup = str(BeautifulSoup(enex, "html.parser"))
    soup_sub = re.sub(r'(<a href="evernote.*?>)(.*?)(</a>?)', r"[[\2]]", soup)
    soup_sub = re.sub(r"(<h1>?)(.*?)(</h1>?)", r"\2", soup_sub)
    with open(f"{os.path.dirname(file)}/bear/{file.name}", "x") as new_enex:
        new_enex.write(soup_sub)
```

**Success!**

#### Updating regular expressions to catch all note links

The initial implementation converted most of the links in my Evernote exports, but missed some. Further inspection showed that Evernote was inserting additional attributes between the opening anchor tag `a` and the `href`, like:

```html
<a style="font-weight: bold;" href="evernote:///">Title</a>
```

I updated the pattern matching behavior to accommodate additional attributes in the anchor tag. The regex only needed a minor update, from `(<a href="evernote.*?>)(.*?)(</a>?)` to `(<a.*?href="evernote.*?>)(.*?)(</a>?)`.

#### No soup for you

After implementing regular expressions, I realized that I actually didn't need Beautiful Soup at all. I could just read the file as a string, modify the string, and then write the string to a new file. Simple! I made a few touch-ups, such as using <a href="https://docs.python.org/3/library/pathlib.html" rel="external" target="_blank"><code>pathlib</code></a> instead of `os` for file path operations, but at this point, the code was ready to run.

#### Updating regular expressions for wiki links

Bear has made lots of progress since I first imported my notes. <a href="https://web.archive.org/web/20240531045315/https://bear.app/faq/how-to-link-notes-together/" rel="external" target="_blank">Note links</a> have been updated with some new "wiki link" features:

- Forward slashes reference headings within notes (`[[note title/heading]]`)
- Pipes configure aliases (different link titles) (`[[note title|alias]]`)

If any notes have forward slashes or pipes in the titles, links to those notes need to escape (ignore) forward slashes and pipes to avoid conflicting with how they are used in Bear wiki links. Bear uses backslashes to escape characters in note links, so backslashes themselves also need to be escaped.

Previously, the script was simply formatting links by placing the note title (`\2`, the second capture group in the regular expression) inside double brackets, like `[[note title]]`.

```py
enex_contents_with_converted_links = re.sub(
    r'(<a.*?href="evernote.*?>)(.*?)(</a>?)', r"[[\2]]", enex_contents
)
```

The second argument to `re.sub` can also accept a "<a href="https://docs.python.org/3/glossary.html#term-callable" rel="external" target="_blank">callable</a>" (function or other object with a `__call__` method). One way to pass a callable to `re.sub` is to use a <a href="https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions" rel="external" target="_blank">lambda expression</a>:

```py
enex_contents_with_converted_links = re.sub(
    r'(<a.*?href="evernote.*?>)(.*?)(</a>?)',
    lambda match: f"[[{match.group(2).replace("\\", r"\\").replace(r"/", r"\/").replace(r"|", r"\|")}]]",
    enex_contents,
)
```

The lambda expression might be considered difficult to read. Let's move the callable to a separate function definition, with a leading underscore to indicate that the function is <a href="https://docs.python.org/3/tutorial/classes.html#private-variables" rel="external" target="_blank">private</a> (only for use within this script). As explained in the <a href="https://docs.python.org/3/library/re.html" rel="external" target="_blank"><code>re</code> docs</a>, "If _repl_ is a function, it is called for every non-overlapping occurrence of _pattern_. The function takes a single `Match` argument, and returns the replacement string." The function should therefore identify the second capture group within the `Match` argument, escape special characters, and return the formatted wiki link, like this:

```py
def _format_note_link(match: re.Match) -> str:
    note_title = match.group(2)
    escaped_note_title = note_title.replace("\\", r"\\")
    escaped_note_title = escaped_note_title.replace("/", r"\/")
    escaped_note_title = escaped_note_title.replace("|", r"\|")
    return f"[[{escaped_note_title}]]"
```

We'll then reference the function as the second argument to `re.sub`.

```py
enex_contents_with_converted_links = re.sub(
    r'(<a.*?href="evernote.*?>)(.*?)(</a>?)', _format_note_link, enex_contents
)
```

Note links will now be properly escaped.

[^1]: From _Stand on Zanzibar_ by John Brunner, Continuity 3
