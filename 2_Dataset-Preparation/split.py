import sys
import splitfolders

if len(sys.argv) != 7:
    print("usage: split.py in_dir out_dir train_perc val_perc test_perc seed")
else:
    in_dir = sys.argv[1]
    out_dir = sys.argv[2]

    train_perc = sys.argv[3]
    val_perc = sys.argv[4]
    test_perc = sys.argv[5]

    seed = sys.argv[6]

    splitfolders.ratio(in_dir, output=out_dir, 
                   seed=int(seed), ratio=(int(train_perc)/100, int(val_perc)/100, int(test_perc)/100), 
                   group_prefix=None)