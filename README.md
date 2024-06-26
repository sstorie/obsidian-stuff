# obsidian-stuff
This is a collection of resources I use to take more usable notes with Obsidian. 

# Plugins
Here's a listing of the plugins I currently use (in alphabetical order). This is a fairly long list, but it grew over time and I don't find myself adding/removing too much these days.

| Plugin | How I use it | URL |
|--------|--------------|-----|
| Advanced Tables | This provides some UI enhancements when working with tables. I don't use it often, but it's handy. | https://github.com/tgrosinger/advanced-tables-obsidian |
| Calendar | Provides a UI panel to quickly open weekly and daily notes. You can easily create new daily/weekly notes from your templates too. Great for creating the daily notes you need ahead of time. | https://github.com/liamcain/obsidian-calendar-plugin |
| Dataview | Query your notes. It's the foundation for my daily use cases today. | https://github.com/blacksmithgu/obsidian-dataview |
| Image Toolkit | This adds useful features around images in your notes. The best feature I like is being able to click the image within the note and see if full screen. | https://github.com/sissilab/obsidian-image-toolkit |
| Linter | Just like code linting, this helps ensure certain formatting rules are applied to your notes automatically. I use it for that and to make sure certain YAML metadata is always added. | https://github.com/platers/obsidian-linter |
| Meta Bind | I use this to create buttons that drive actions, but I think it can do more than that. This is how I quickly create meeting notes from my daily notes. | https://github.com/mProjectsCode/obsidian-meta-bind-plugin |
| Mononote| This makes sure a note is only open in one tab at a time. Simple tweak that helps reduce confusion as you're moving from note to note from the daily one. | https://github.com/czottmann/obsidian-mononote |
| Omnisearch | Powerful search tool that includes your notes (of course), but also OCR within images and any PDFs you've added when combined with the Text Extractor plugin. | https://github.com/scambier/obsidian-omnisearch |
| Periodic Notes | This adds the concept of weekly and monthly notes to the base functionality of Obsidian. I use it for weekly notes today. | https://github.com/liamcain/obsidian-periodic-notes |
| QuickAdd | Add commands that can quickly create notes based on highlighted text. I use this to add new people to my vault. | https://github.com/chhoumann/quickadd |
| Smart Typography | This is a simple one that converts certain strings to others, including some basic ligatures. | https://github.com/mgmeyers/obsidian-smart-typography |
| Style Settings | To be honest, this might be there just to support a theme I tried (or am using). I haven't done any serious tweaking of the styles within Obsidian. | https://github.com/mgmeyers/obsidian-style-settings |
| Templater | This is what powers the templates I use today. It builds upon the basic template functionality with more useful features. | https://github.com/SilentVoid13/Templater |
| Text Extractor | This is a companion plugin that makes Omnisearch more powerful. | https://github.com/scambier/obsidian-text-extractor |
| Various Complements | This adds an auto-complete feature when writing like and IDE does when writing code. | https://github.com/tadashi-aikawa/obsidian-various-complements-plugin |

# Scripts to help automate common things for me
## Zoom AI summaries
My workplace has embraced AI tools and one I use by default is Zoom's AI companion to summarize the discussions during a meeting and email them to me. By default these come in a nice looking HTML-based format, but I can't just copy-paste this content into a Markdown note. To help I used AI to generate a quick python script to rip through the content and use regex's to convert things to Markdown. That script is [included in this repository](scripts/convert-zoom-ai-summary.py) in case you're interested.

I use a Mac for my daily tasks so I map the execution of this script to a Shortcut that's easy to run on demand.

# Blogs and Resources I found helpful
These are in no particular order:
- Dann Berg's site - https://dannb.org/start-here/
  - I stole his daily notes early on but he has a [video showing his obsidian vault too](https://www.youtube.com/watch?v=VdJoWe0Wwkg).
- Lou Plummer's blog - https://amerpie2.micro.blog/
  - He has lots of great tips on not just using Obsidian but integrating it with other tools to make powerful workflows.
- MacSparky's Obsidian Field Guide - https://learn.macsparky.com/p/obsidianfg
  - This costs money, but it was helpful to see a more professional take on how to use Obsidian and his guests show you different use cases people have.
- FromSergio's YouTube Playlist on Obsidian - https://www.youtube.com/watch?v=ctetnQfSdfM&list=PL7oLu8NfQd84_gsyqBVSVgUmCCgcvSZMx
  - He has several videos on Obsidian and several popular plugins