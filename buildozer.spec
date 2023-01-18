[app]

title = Osmeñian

package.name = AstigPree

package.domain = max.eric.astigpree

source.dir = .

source.include_exts = py,png,jpg,kv,atlas, jpeg, ttf, otf, mp3

source.exclude_dirs = sample_data , drive , bin

version = 1.0

requirements = python3, kivy , plyer, android

presplash.filename = mysplash.jpeg

icon.filename = myicon.jpeg

orientation = portrait

osx.python_version = 3

osx.kivy_version = 1.9.1

android.permissions = INTERNET , READ_EXTERNAL_STORAGE , WRITE_EXTERNAL_STORAGE

android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

warn_on_root = 1


