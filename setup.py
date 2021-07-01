from setuptools import setup

package_name = 'ros_cv'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gustavo',
    maintainer_email='gustavo@todo.todo',
    description='publish data according to num',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = ros_cv.gesture_volume_detector:main',
        ],
    },
)
