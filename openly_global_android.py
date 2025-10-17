import zipfile
import os

# Create folder structure for Openly Global
project_name = 'OpenlyGlobal'
dirs = [
    f'{project_name}/app/src/main/java/com/openlyglobal/app',
    f'{project_name}/app/src/main/res/drawable',
    f'{project_name}/app/src/main/res/layout',
    f'{project_name}/app/src/main/res/values'
]

for d in dirs:
    os.makedirs(d, exist_ok=True)

# Create placeholder files
files = {
    f'{project_name}/app/src/main/res/layout/activity_splash.xml': '<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"\n    android:orientation="vertical"\n    android:layout_width="match_parent"\n    android:layout_height="match_parent"\n    android:gravity="center"\n    android:background="@color/purple">
    <ImageView android:src="@drawable/logo" android:layout_width="200dp" android:layout_height="200dp"/>
</LinearLayout>',

    f'{project_name}/app/src/main/res/values/colors.xml': '<resources>\n    <color name="purple">#6A0DAD</color>\n    <color name="blue">#3B82F6</color>\n</resources>',

    f'{project_name}/app/src/main/res/values/strings.xml': '<resources>\n    <string name="app_name">Openly Global</string>\n    <string name="tagline">Just you, your thoughts, and calm listening. Real talk, no judgment.</string>\n</resources>',

    f'{project_name}/app/src/main/res/values/styles.xml': '<resources>\n    <style name="AppTheme" parent="Theme.MaterialComponents.DayNight.DarkActionBar">\n        <item name="colorPrimary">@color/purple</item>\n        <item name="colorPrimaryVariant">@color/blue</item>\n        <item name="colorAccent">@color/blue</item>\n    </style>\n</resources>',

    f'{project_name}/app/src/main/AndroidManifest.xml': '<manifest xmlns:android="http://schemas.android.com/apk/res/android"\n    package="com.openlyglobal.app">\n    <application\n        android:label="@string/app_name"\n        android:theme="@style/AppTheme">\n        <activity android:name=".SplashActivity">\n            <intent-filter>\n                <action android:name="android.intent.action.MAIN"/>\n                <category android:name="android.intent.category.LAUNCHER"/>\n            </intent-filter>\n        </activity>\n    </application>\n</manifest>',

    f'{project_name}/README.md': '# Openly Global - Android App\n\n## How to Build APK\n1. Open `OpenlyGlobal` folder in Android Studio.\n2. Let Gradle sync.\n3. Press `Build > Build Bundle(s) / APK(s) > Build APK(s)`.\n4. Find the generated APK in `app/build/outputs/apk/release/`.'
}

for path, content in files.items():
    with open(path, 'w') as f:
        f.write(content)

# Add logo placeholder
logo_path = f'{project_name}/app/src/main/res/drawable/logo.png'
with open(logo_path, 'wb') as f:
    f.write(open('/mnt/data/e5ca3d33-08d9-4532-bd88-2a5ee8e75a75.png', 'rb').read())

# Zip the project
zipf = f'{project_name}.zip'
with zipfile.ZipFile(zipf, 'w', zipfile.ZIP_DEFLATED) as zipfout:
    for root, dirs, files in os.walk(project_name):
        for file in files:
            zipfout.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), project_name))

zipf
