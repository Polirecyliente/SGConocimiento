---
title: WEB COMPONENTS
toc-title: Table of Contents
---

# INTRODUCTION

This document contains the following ways of creating web components: Angular, Flutter.

# INSTALLATION

Flutter can be downloaded from its official website (when this was written, Flutter can be downloaded from https://flutter.dev/docs/get-started/install/linux).

This downloads a file named similar to `flutter_linux_version1-stable.tar.xz`. 

Extract it.

``` {.bash in="in CLI"}
tar xf flutter_linux_2.2.0-stable.tar.xz
```

This creates a directory named `flutter` with the code to execute Flutter.

Check if the `flutter` and `dart` programs are on the path.

``` {.bash in="in CLI"}
which flutter dart
```

If there is no output, then add the `flutter/bin` directory to the path (this following code assumes you have not changed the current directory in the CLI).

``` {.bash in="in CLI"}
echo "export PATH=\"\$PATH:$(pwd)/flutter/bin\"" >> ~/.bashrc
```

Start a new shell session for this to take effect.


----

Flutter can be used to develop web components to be viewed in mobile devices. Android is a common operating system for mobile devices.

To develop for Android, download the Android SDK, designed to develop for Android.

When this was written, the Android SDK can be downloaded from https://developer.android.com/studio, there download Android Studio. Android Studio includes an IDE to develop Android applications, this IDE allows showing in a computer, how the application would look in an Android mobile.