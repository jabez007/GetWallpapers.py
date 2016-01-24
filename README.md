## Synopsis

This script is an attempt to scrape wallpapers from the subreddits that make up the SFW Porn Network.
It's meant to keep your desktop backgrounds fresh, and can even handle multiple monitors without having 
to use extra software.

## Code Example

This script uses the PRAW library to access Reddit's search API, then uses the urllib library to retrieve the images.
The PIL and itertools libraries are used to create combinations of images wide enough to fit across your monitors. 

## Motivation

Ironically, its difficult to install extra software on my desktop at work, but I can browse Reddit all day long. 
So I wrote this script to scrape and create wallpapers that will fit across my three monitors.

## Installation

1. Download tha files of in this repository.
2. Edit the config file
    * Monitor resolution
    * Number of monitors
    * Which subreddits to pull from and how far back to search for images (all time, month, week, day)
    * Where to save images to
3. Run the script
4. Point Windows to use your folder for desktop backgrounds
    * For only one monitor - folder set in config
    * For more monitors - "merged" subfolder of the folder set in config
5. (optional) Set up a scheduled task to periodically run this script and update your wallpapers

## License

The MIT License (MIT)

Copyright (c) 2016 Jimmy McCann

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.