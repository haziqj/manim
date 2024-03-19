# Manim Extension For Quarto

This plugin brings support for beautiful [Manim]() animations to be added to Quarto Reveal.js slide decks. 
Designed to enrich your presentations with high-quality mathematical animations and engaging visual storytelling, this plugin simplifies the inclusion of Manim-generated content directly into your Quarto slides.


## Installing

```bash
quarto add haziqj/manim
```

This will install the extension under the `_extensions` subdirectory.
If you're using version control, you will want to check in this directory.

## Using

In order to use this Manim extension, you will first have to render your animations.
This requires two things:

1. A working [installation](https://docs.manim.community/en/stable/installation.html#local-installation) of Manim itself and all its dependencies.
2. The [`{manim-revealjs}`](https://github.com/RickDW/manim-revealjs) plugin, which can be installed via
   ```bash
   pip install manim-revealjs
   ```



## Example

Here is the source code for a minimal example: [example.qmd](example.qmd).

