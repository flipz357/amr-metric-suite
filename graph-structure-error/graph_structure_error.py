import sys

try:
    import networkx as nx
except ModuleNotFoundError:
    sys.exit("please install networkx")
try:
    import penman
except ModuleNotFoundError:
    sys.exit("please install penman")

import numpy as np
import sys
import argparse

def build_arg_parser():
    """
    Build an argument parser using argparse. Use it when python version is 2.7 or later.

    """
    parser = argparse.ArgumentParser(description="Graph structure error calculator -- arguments")
    parser.add_argument('-f', nargs=2, required=True, type=argparse.FileType('r'),
                        help='Two files containing AMR pairs. AMRs in each file are separated by a single blank line')
    return parser

def get_amrs(inp):
    dats = inp.read().split("\n\n")
    dats = [" ".join([z for z in x.split("\n") if not z.startswith("#")]) for x in dats if x]
    dat=[]
    for d in dats:
        dat.append(penman.decode(d))
    datg = [nx.DiGraph() for x in dat]
    for i,g in enumerate(dat):
        for t in g.triples():
            datg[i].add_edge(t[0],t[2],label=t[1])
    return datg


def get_degr_density_Vsize_Esize(nxgraphs):

    degr = [(2*G.number_of_edges())/G.number_of_nodes() for G in nxgraphs]
    dens = [nx.density(G) for G in nxgraphs]
    Vsize = [len(G.nodes) for G in nxgraphs]
    Esize = [len(G.edges) for G in nxgraphs]

    return np.array(degr), np.array(dens), np.array(Vsize), np.array(Esize)


if __name__ == "__main__":
    parser = build_arg_parser()
    args = parser.parse_args() 
    pred = get_amrs(args.f[0])
    gold = get_amrs(args.f[1])
    dip, dep, Vp, Ep = get_degr_density_Vsize_Esize(pred)
    dig, deg, Vg, Eg = get_degr_density_Vsize_Esize(gold)
    print("A stats: \n\
            \tavg. degree={}\n\
            \tavg. density={}\n\
            \tavg. |V|={}\n\
            \t avg. |E|={}".format(
                np.mean(dip)
                , np.mean(dep)
                , np.mean(Vp)
                , np.mean(Ep)))
    print("B stats: \n\
            \tavg. degree={}\n\
            \tavg. density={}\n\
            \tavg. |V|={}\n\
            \t avg. |E|={}".format(
                np.mean(dig)
                , np.mean(deg)
                , np.mean(Vg)
                , np.mean(Eg)))

    print("avg. absolute error: \n\
            \tdegree={}\n\
            \tdensity={}\n\
            \t|V|={}\n\
            \t|E|={}".format(
                np.mean(np.abs(dig-dip))
                , np.mean(np.abs(deg-dep))
                , np.mean(np.abs(Vg-Vp))
                , np.mean(np.abs(Eg-Ep))))
