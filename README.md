This Week in GraphQL
=================

Content for [this-week-in-graphql.org](http://this-week-in-graphql.org). Made available under CC-BY-SA.

All code Copyright 2014 Ember Arlynx, made available under [the MIT
license](http://mit-license.org/).

## TWiR Editors

* [doc-jones](https://github.com/doc-jones)
* [TBD](https://google.com)
* [TBD](https://google.com)


### Language Reviewers

* We are looking for contributors to help translate the newsletter into other languages: Spanish, Japanese, German, Portuguese, and Chinese and more. Reach out the editors if you would like to contribute a translation.

## PRs for next issue are now being accepted

To propose content for inclusion in the next newsletter (found in the `drafts/`
folder), create a new [Pull Request](https://github.com/doc-jones/TWiG/pulls) updating the relevant section in the 
draft.

Alternately, tweet us [@graphql](https://twitter.com/graphql).

### What do we look for when considering whether to include something in This Week in GraphQL?

This Week in GraphQL is intended to highlight the incredible work of the GraphQL Community. 

What we are generally looking for includes:

* how-to intros (and advanced deep dives) into GraphQL concepts and areas
* GraphQL walkthroughs that explain concepts in different ways than well known resources like [GraphQL documentation](https://graphql.org), [GraphQL Concepts](https://learning.postman.com/open-technologies/specifications/graphql/concepts/), and [GraphQL by Example](https://google.com)
* updates on tooling when in long form or framed as a tutorial (for more details, see what we are not looking for below)
* GraphQL-related podcast episodes
* GraphQL-related screenshots and videos
* GraphQL meetup recordings
* GraphQL meetup announcements
* Presenter slide decks on GraphQL
* Observations and thoughts on GraphQL and the GraphQL community
* Calls for participation in GraphQL open source projects
* GraphQL job announcements
* and more!

What we are generally NOT looking for includes:

* Anything that violates the [GraphQL Community Code of Conduct](https://www.rust-lang.org/policies/code-of-conduct)
* Rants or anything degrading to any part or member of the Community. Rather than submitting an article about what is wrong with something, we would much rather you write something that explains how you'd make it better.
* Duplicates of recent posts (even with the wording changed slightly)
* Anything behind a paywall (this includes Medium's paid article / members-only mechanism)
* Anything that requires information to be shared/captured (like an email address) in order to access

**Projects/Tooling Updates**

There are further guidelines for the Projects/Tooling Updates Section

We include:
* Updates on tooling when in long form or framed as a tutorial (this can be through a blog, through GitHub, through a newsletter, and more) - it must have a high amount of GraphQL specific info (examples in GraphQL, notes on things learned about GraphQL in the process of creating/updating the project, etc.)
* Updates on tooling that call out specific contributors - it is wonderful to highlight all the great people contributing to GraphQL OSS projects (Note - the update still must include a high amount of GraphQL specific info)
* Changelogs of projects (though we strongly prefer the changelogs be accompanied with details on the changes, guides to using the changes, etc.)

We do not include:
* Links that are solely to a GitHub repo or package on npm, pypi or the like. While we would love to include these, there are too many being created/updated every week for us to include them all. We encourage you to write up an introduction to your project with examples, information you learned through creating the project, changes you recently made to the project, etc.

Notes:
* A small description of the project or the update in your link is encouraged (for example: FooBar 1.0: adding support for Baz)
* We discourage submitting links and link descriptions that are solely of a commercial/sales nature

These are meant to be guidelines, if you are ever not sure about whether something should be included please feel free to open a pull request anyway and we can discuss it!

The editors of This Week in GraphQL do reserve the right to make the decision about whether to include something or not, but we intend to do so in a way that is as transparent as possible.

## Link style guidelines:

The link text should be the same as the page's title. If the title seems to need additional context (for example, if the title is "What's New" and should have the project name added), please ask in the PR comments.

Links should use the most canonical form. For example, if `example.tech` redirects to `www.example.com`, then the latter is preferred.

Links should not contain unnecessary tracking parameters, e.g. `utm_source`, `utm_campaign`.

Some prefixes are used, and should be placed to the left of the link.
- `[video]` for videos
- `[audio]` for podcasts or other audio.
- `[series]` for articles that are one of a series.
- 2-letter languages codes (e.g. `[ZH]`, `[ES]`, `[FR]`) for content in a language other than English.

## Community sub-categories

Editors will sort community links into sub-categories. The following sub-categories are currently used:
- **Official** -- rust-lang.org blog posts and other official GraphQL team communications.
- **Foundation** -- foundation.rust-lang.org blog posts and other official foundation communications.
- **Project/Tooling Updates** -- News about the progress of a GraphQL project. Must be more informative than just a changelog.
- **Newsletters** -- Regularly scheduled articles about an area of GraphQL development, e.g. posts titled "This Month in ___".
- **Research** -- Academic Papers that are about GraphQL or contain significant GraphQL content.
- **Observations/Thoughts** -- Articles about GraphQL.
- **GraphQL Walkthroughs** -- Articles that include a significant amount of GraphQL source code, that walk the reader through building something.
- **Miscellaneous** -- Links that don't clearly fit in other sub-categories.

Most blog posts about GraphQL belong in **GraphQL Walkthroughs** if they show how something is done (including source code), otherwise **Observations/Thoughts**. Articles that don't contain much GraphQL content, or news articles that mention GraphQL, won't always be accepted, but when they are they can be placed in the **Miscellaneous** sub-category.

If a set of related links is published (e.g. from a large GraphQL conference), the editors may choose to invent a new category just for that issue.

## How I get PR lists:

```
git log --author=bors --since='MM/DD/YYYY 12:00PM' --until='MM/DD/YYYY 12:00PM' --pretty=oneline > ~/entropy/twir.txt
# edit in vim to get rid of everything but PR number, copy into clipboard
for pr in $(xsel -ob); do firefox https://github.com/mozilla/rust/pull/$pr; sleep 0.07; done
# wait a long time...
# write TWiG
```

Alternatively use GitHub search:

```
https://github.com/rust-lang/rust/pulls?q=is%3Apr+is%3Amerged+updated%3A2014-11-03..2014-11-10
```

## How I get new contributors:

Use the included `new_contribs.sh` script:

  new_contribs.sh 6/21/2014

## Building

To ensure consistency across development setups, we use a [Docker](https://www.docker.com) container-based
workflow for building the website and email newsletter. Similarly, we use a `makefile` to Ensure you have Docker installed on your system if
you intend to build the website or email newsletter.

### Building the website

*Before attempting to build the website, ensure Docker is in a running state on your system.*

* Enter the `publishing/` directory:
  ```sh
  cd publishing
  ```
* Run the Docker build and website local-host command:
  ```sh
  make build && make generate-website && make host-content
  ```
* View the website locally at default http://localhost:8000, or specific posts
  at http://localhost:8000/blog/{YEAR}/{MONTH}/{DAY}/{ISSUE}/.

Note: If looking to test the website's search functionality locally, you will need to adjust the [`TESTING_LOCALLY`](https://github.com/rust-lang/this-week-in-rust/blob/dc127f17fcabbf0f058eb3d5a3febba434ddca83/pelicanconf.py#L7)
variable to `True`.

### Building the newsletter

*Before attempting to build the email newsletter, ensure Docker is in a running state on your system.*

* Enter the `publishing/` directory:
  ```sh
  cd publishing
  ```
* Run the Docker build and website local-host command:
  ```sh
  make build && make generate-email && make host-content
  ```
* View the email newsletter formatting of specific posts at
  http://localhost:8000/blog/{YEAR}/{MONTH}/{DAY}/{ISSUE}/.
