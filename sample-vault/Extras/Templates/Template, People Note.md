---
company: SPS Commerce
location: 
title: 
team: 
email: 
website: 
aliases:
---

tags: [[People MOC]]

# <% tp.file.title %>

<% await tp.file.move("/Extras/People/" + tp.file.title) %>

## Org Details


## Notes

## Meetings
```dataview
TABLE file.cday as Created, summary AS "Summary"
FROM "Timestamps/Meetings" where contains(file.outlinks, [[<% tp.file.title %>]])
SORT file.cday DESC
```

## Emails
```dataview
TABLE file.cday as Created, summary as "Summary"
FROM "Timestamps/Emails" where contains(file.outlinks, [[<% tp.file.title %>]])
SORT file.cday DESC
```