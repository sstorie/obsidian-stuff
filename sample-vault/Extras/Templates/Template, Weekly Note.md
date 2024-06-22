---
start-of-week: <% moment(tp.file.title, "YYYY-[W]ww").startOf("iweek").format("YYYY-MM-DD")%>
title: <% tp.file.title %>
aliases: []
tags: []
---

Year: [[{{date:yyyy}}]]
Month: [[{{monday:yyyy-MM}}]]
Days: [[{{monday:YYYY-MM-DD-dddd}}]], [[{{tuesday:YYYY-MM-DD-dddd}}]], [[{{wednesday:YYYY-MM-DD-dddd}}]], [[{{thursday:YYYY-MM-DD-dddd}}]], [[{{friday:YYYY-MM-DD-dddd}}]], [[{{saturday:YYYY-MM-DD-dddd}}]], [[{{sunday:YYYY-MM-DD-dddd}}]]

# <% tp.file.title %>

## Items to Discuss

## Notable Items

## Project Updates

## Highlighted Meetings
```dataview
TABLE summary AS "Summary"
FROM "Timestamps/Meetings" where meeting-date.weekyear = this.start-of-week.weekyear and summary-highlight = true
SORT date DESC
```

%% A comment to prevent this from being included in the PDF export

> [!NOTE]- All Other Meetings
> ```dataview
> TABLE summary AS "Summary"
> FROM "Timestamps/Meetings" where meeting-date.weekyear = this.start-of-week.weekyear and summary-highlight = false
> SORT date DESC
> ```

%%