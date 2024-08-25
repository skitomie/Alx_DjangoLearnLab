Permissions and Groups Setup

- Groups:

  - `Editors`: Can create and edit `SomeModel` instances.
  - `Viewers`: Can view `SomeModel` instances.
  - `Admins`: Full access including view, create, edit, and delete.

- Custom Permissions:

  - `can_view`: Permission to view `SomeModel` instances.
  - `can_create`: Permission to create `SomeModel` instances.
  - `can_edit`: Permission to edit `SomeModel` instances.
  - `can_delete`: Permission to delete `SomeModel` instances.

- Views:
  - The `view_somemodel` view checks for the `can_view` permission.
  - The `edit_somemodel` view checks for the `can_edit` permission.
