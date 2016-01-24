# https://www.reddit.com/r/sfwpornnetwork/wiki/network
import json
import praw
import os
import urllib
from PIL import Image
from itertools import combinations


def get_wallpapers(sub, cnf):
    resolution = "%sx%s" % (cnf["resolution"]["width"],
                            cnf["resolution"]["height"])

    if cnf["monitors"] > 1:
        path = os.path.join(cnf["path"],
                            sub)
    else:
        path = cnf["path"]
        
    if not os.path.isdir(path):
        os.mkdir(path)
        period = 'all'
    else:
        period = cnf["period"]

    if period == "all":
        print "Searching %s for %s %s images of all time" % (sub,
                                                             cnf["sort"],
                                                             resolution)
    elif period == "day":
        print "Searching %s for %s %s images of the past 24 hours" % (sub,
                                                                      cnf["sort"],
                                                                      resolution)
    else:
        print "Searching %s for %s %s images of the past %s" % (sub,
                                                                cnf["sort"],
                                                                resolution,
                                                                period)    
    
    before = os.listdir(path)
    
    for s in R.search(resolution, subreddit=sub, sort=cnf["sort"], period=cnf["period"]):  # https://www.reddit.com/dev/api#GET_search
        if any(s.url.endswith(ext) for ext in cnf["exts"]):
            file_name = s.url.split("//")[1].replace("/","_")
            if file_name not in os.listdir(path):
                download_url = urllib.URLopener()
                try:
                    download_url.retrieve(s.url,
                                          os.path.join(path,
                                                       file_name))
                    print "Downloaded %s" % file_name
                except IOError as e:
                    with open("errors", "a") as err:
                        err.write("%s: %s\n" % (s.url, e))

    after = os.listdir(path)
    new_images = list(set(before)^set(after))
    if cnf["monitors"] > 1 and new_images:
        create_wallpapers(path,
                          cnf)
'''
sort = [#relevance (default),
        hot,
        #top,
        #new,
        #comments]
period = [all (deafult),
          hour,
          day,
          week,
          month,
          year]
'''


def create_wallpapers(pull_from, cnf):
    images = [f for f in os.listdir(pull_from) if (os.path.isfile(os.path.join(pull_from, f)) and f[-4:] in cnf["exts"])]
    with open("used_combinations", 'r') as used_f:
        used_combos = [tuple(combo.strip().split(", ")) for combo in used_f.readlines()]

    path = os.path.join(cnf["path"],
                        "Merged")
    if not os.path.isdir(path):
        os.mkdir(path)

    filenumber = len(os.listdir(path)) + 1
    for s in combinations(images, cnf["monitors"]):
        if s in used_combos:
            continue
        
        combo_images = [Image.open(os.path.join(pull_from, img_f)) for img_f in s]
        desktop_bg = Image.new(combo_images[0].mode,
                               (cnf["resolution"]["width"] * cnf["monitors"], cnf["resolution"]["height"]))
        for m in range(cnf["monitors"]):
            desktop_bg.paste(combo_images[m],
                             (cnf["resolution"]["width"] * m, 0))
        desktop_bg.save(os.path.join(path,
                                     "img %s.png" % filenumber))
        print "Created 'img %s.png' using %s" % (filenumber, s)

        used_combos.append(s)
        with open("used_combinations", "a") as used_f:
            used_f.write(", ".join(s)+"\n")
        filenumber += 1


if __name__ == "__main__":
    with open("config", 'r') as f:
        config = json.load(f)
    R = praw.Reddit("jabez007_GetWallpapers")
    for sr in config["subreddits"]:
        get_wallpapers(sr, config)
    raw_input("Press Enter to Continue...")    
