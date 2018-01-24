# homepage

**homepage** generates a customized portal for your default page that's
opened when you open a new tab or browser window.

The list of categories and pages is specified and maintained in a
YAML-formatted file (`index.yaml`).

## Dependencies

* python3
* PyYaml (`convert.py`, `generate.py`)
* BeautifulSoup (`convert.py`)

## Usage

To generate your homepage (`generate.py`):

1. Edit `index.yaml` with your categories and links (you can also
generate your list of links from your exported bookmarks.html via
`python3 convert.py bookmarks.html > index.yaml`)
2. (*optional*) Modify `index.m4` with your custom styles
3. Run `make`
4. Point your browser's home page to `/path/to/homepage/index.html`:

   *Firefox*: Preferences > "Home page"

   *Chrome*:
   1. Settings > "On startup" > "Open a specific page or set of pages"
   2. Settings > "Appearance" > "Show home button" > "Enter custom web address"

*Note*: Setting your New Tab page typically requires an add-on or
extension.

Firefox users can use
[New Tab Homepage](https://addons.mozilla.org/en-US/firefox/addon/new-tab-homepage/),
although as of 2018-Jan-17 this doesn't seem to be working.

You can click on each site link individually, or click on the category
name to open all the sites in each category at once.

## Example

`index.yaml`:
```yaml
"procrastination":
  - "hacker news": https://news.ycombinator.com
  - "newsblur": https://newsblur.com
  - "arstechnica": https://arstechnica.com

"reddit":
  - "top": https://reddit.com/
  - "popular": https://reddit.com/r/popular
  - "all": https://reddit.com/r/all
  - "random": https://reddit.com/r/random
```

`index.html`:
![screenshot of a generated homepage portal](example.png)

## Contributing

All of the template code (CSS, JS, HTML) can be found in `index.m4`.
The webpage is styled very simply with CSS Grid.

The `Makefile` executes `generate.py`, which outputs an HTML snippet,
and uses `m4` to generate the final HTMl.

Feel free to contribute code or send comments, suggestions, bugs to
calvin@isi.edu.

## LICENSE

[CC0 1.0 Universal](./LICENSE)
