---
title: '<% tp.date.now("YYYY-MM-DD") + " " + tp.file.title %>'
meeting-date: <% tp.file.creation_date("YYYY-MM-DD") %>
summary: 
summary-highlight: false
client-call: false
type: meeting
aliases: []
tags: []
---

Week: [[<% tp.date.now("YYYY-[W]ww") %>]]
<% await tp.file.move("/Timestamps/Meetings/" + tp.date.now("YYYY-MM-DD") + " " + tp.file.title) %>
# [[<% tp.date.now("YYYY-MM-DD") + " " + tp.file.title %>]]

## Attendees


## Agenda/Questions


## Notes
