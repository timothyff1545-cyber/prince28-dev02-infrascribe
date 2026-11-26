You read one document from InfraScribe's collection and fill in a small record about it.

What InfraScribe does: A Terraform assistant for AWS that answers resource and argument questions from the provider docs and returns HCL that passes validation.

Rules:
- Reply with one JSON object and nothing else: no explanation, no Markdown fences.
- Use only what the document says. If it does not say, use null for the year and [] for a list.
- summary: one or two plain sentences, at most 300 characters.
- topics: 1 to 6 short topics.
- Every list holds short values copied from the document, at most 8.

What each field means:
- doc_kind: what kind of document this is.
- year: the year it was published or came into force.
- language: the main language of the text (en, ta, hi or other).
- resource_type: every "resource type" this document is mainly about.
- argument: every "argument" this document is mainly about.
- required: every "required" this document is mainly about.
- version_added: every "version added" this document is mainly about.
- deprecated_in: every "deprecated in" this document is mainly about.
- service: every "service" this document is mainly about.
