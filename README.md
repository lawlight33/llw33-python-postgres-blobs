## Postgres blobs Python example

The following is an example of uploading files as blobs to the Postgres database.

Basically, Postgres has two ways of dealing with blobs:
- bytea data type https://www.postgresql.org/docs/current/datatype-binary.html.
- lo (large objects) https://www.postgresql.org/docs/current/lo.html.

Keep in mind that you have to have your file uploaded to the database server when dealing with LOs.