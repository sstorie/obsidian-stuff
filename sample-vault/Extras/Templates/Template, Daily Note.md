---
date: <% tp.file.creation_date("YYYY-MM-DD") %>
title: <% moment(tp.file.title,'YYYY-MM-DD').format("dddd, MMMM DD, YYYY") %>
aliases: []
tags: []
---

tags: [[+Daily Notes]]

```meta-bind-button
label: New Meeting
hidden: false
class: ""
tooltip: ""
id: ""
style: default
actions:
  - type: templaterCreateNote
    templateFile: Extras/Templates/Template, Meeting Note.md
    folderPath: Timestamps/Meetings
    fileName: TKTK
    openNote: true
```

```meta-bind-button
label: New 1x1 Meeting
hidden: false
class: ""
tooltip: ""
id: ""
style: default
actions:
  - type: templaterCreateNote
    templateFile: Extras/Templates/Template, 1x1 Meeting Note.md
    folderPath: Timestamps/Meetings
    fileName: TKTK
    openNote: true
```
# <% moment(tp.file.title,'YYYY-MM-DD').format("dddd, MMMM DD, YYYY") %>

```dataviewjs
/*
    previous/next note by date for Daily Notes
    Also works for other files having a `date:` YAML entry.
    MCH 2021-06-14
*/
var none = '(none)';

var p = dv
	.pages("[[+Daily Notes]]")
	.where(p => p.file.day)
	.map(p => [p.file.name, p.file.day.toISODate()])
	.sort(p => p[1]);

var t = dv.current().file.day ? 
	dv.current().file.day.toISODate() : 
	luxon.DateTime.now().toISODate();
	
// Obsidian uses moment.js; Luxon’s format strings differ!
var format = app['internalPlugins']['plugins']['daily-notes']['instance']['options']['format'] || 'YYYY-MM-DD';

var current = '(' + moment(t).format(format) + ')';
var week = moment(t).format("YYYY-[W]ww");
var nav = [];
var today = p.find(p => p[1] == t);
var next = p.find(p => p[1] > t);
var prev = undefined;
p.forEach(function (p, i) {
    if (p[1] < t) {
        prev = p;
    }
});
nav.push(prev ? '[[' + prev[0] + ']]' : none);
//nav.push(today ? today[0] : none);
nav.push(today ? today[0] : current);
nav.push(next ? '[[' + next[0] + ']]' : none);

//dv.list(nav);
//dv.paragraph(nav.join(" · "));
dv.paragraph(nav[0] + ' ← ' + nav[1] + ' ([[' + week + ']]) ' + ' → ' + nav[2])
```

## Notes

## Meeting Summaries
```dataview
TABLE summary AS "Summary"
FROM "Timestamps/Meetings" where meeting-date = this.date
SORT file.cday DESC
```


---
> [!NOTE]- Notes Created Today
> ```dataview
> List FROM "" WHERE file.cday = this.file.cday SORT file.ctime asc
> ```

> [!NOTE]- Notes Modified Today
> ```dataview
> List FROM "" WHERE file.mday = this.file.mday SORT file.mtime asc
> ```
