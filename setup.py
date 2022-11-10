from setuptools import setup

setup(
    name='yt_dlp_server',
    version='0.1',
    description='An API server based on yt-dlp',
    long_description='Get the videos from different sites using a server running yt_dlp',
    author='NishatAhmed',
    author_email='nishatahmed92297@gmail.com',
    url='https://github.com/nishatahmed297/yt-dlp-server',
    packages=['yt_dlp_server'],
    entry_points={
        'console_scripts': [
            'yt-dlp-server = yt_dlp_server.server:main',
        ],
    },

    install_requires=[
        'Flask',
        'yt_dlp >= 2022.10.4',
    ],

    classifiers=[
        'Topic :: Multimedia :: Video',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: Public Domain',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
)
