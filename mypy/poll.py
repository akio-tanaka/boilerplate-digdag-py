import os
import glob

ext = ".csv"


def do(folderpath):
    print(folderpath)
    lists = glob.glob(os.path.join(folderpath, "*"))
    stats = list(map(os.path.getmtime, lists))  # mtime: update datetime
    print("info: done to get item information")

    output_filepath = folderpath.replace("\\", "-").replace(":", "-") + ext
    print("output file: {}".format(output_filepath))

    is_saved = False
    with open(output_filepath, "w") as f:
        f.write("item,epoch time\n")
        for i in range(len(lists)):
            f.write("{}\n".format(lists[i] + "," + str(stats[i])))
        print("info: done to wriote {}".format(output_filepath))
        is_saved = True
    if not is_saved:
        print("error: failed to write {}".format(output_filepath))
