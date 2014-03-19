import setuptools

setuptools.setup(
    name="mon-notification",
    version="0.1",
    packages=setuptools.find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'mon-notification = mon_notification.main:main'
        ],
    },
    scripts=['tools/mon_notification_offsets.py'],
    test_suite='nose.collector'
)
