[app]
title = EclipseLab
package.name = eclipselab
package.domain = org.carlosfelipe
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Android
android.api = 35
android.minapi = 23
android.ndk = 27c
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

# No permissions are needed for this educational app.
# android.permissions =

[buildozer]
log_level = 2
warn_on_root = 1
