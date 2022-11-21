# [style guide | Style guides for Google-originated open-source projects](https://google.github.io/styleguide/pyguide.html#316-naming)

|Type                       |  Public             | Internal                          |
|---------------------------|---------------------|-----------------------------------|
|Packages                   | `lower_with_under`  |                                   |
|Modules                    | `lower_with_under`  | `_lower_with_under`               |
|Classes                    | `CapWords`          | `_CapWords`                       |
|Exceptions                 | `CapWords`          |                                   |
|Functions                  | `lower_with_under()`| `_lower_with_under()`             |
|Global/Class Constants     | `CAPS_WITH_UNDER`   | `_CAPS_WITH_UNDER`                |
|Global/Class Variables     | `lower_with_under`  | `_lower_with_under`               |
|Instance Variables         | `lower_with_under`  | `_lower_with_under` (protected)   |
|Method Names               | `lower_with_under()`| `_lower_with_under()` (protected) |
|Function/Method Parameters | `lower_with_under`  |                                   |
|Local Variables            | `lower_with_under`  |                                   |
