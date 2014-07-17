import glob
import os.path


def averDeg(filename):
    f = open(filename)
    averDeg = 0.0
    count = 0

    for l in f.xreadlines():
        averDeg += float(l.strip())
        count += 1

    return averDeg / count


def averDegVar(filename):
    f = open(filename)
    averDeg = 0.0
    sqAverDeg = 0.0
    count = 0

    for l in f.xreadlines():
        averDeg += float(l.strip())
        sqAverDeg += float(l.strip()) ** 2
        count += 1

    averDeg /= count
    sqAverDeg /= count

    var = (sqAverDeg - averDeg ** 2)

    return var


def averDegBias(filename, realVal):
    f = open(filename)
    averBias = 0.0
    count = 0

    for l in f.xreadlines():
        averBias += float(l.strip()) - realVal
        count += 1

    return averBias / count /realVal


def makeJP_AverDeg_Plot(fileprefix, outputFilename):
    '''
    OUTPUT:
        JP, NOR_Aver_Deg, CW_Aver_Deg, RM1_Aver_Deg
    '''

    output = open(outputFilename, 'w')

    for i in range(1, 21):
        jp = i * 0.01
        nad = averDeg('%s.rw%0.3f' % (fileprefix, jp))
        cad = averDeg('%s.rw%0.3f.cw' % (fileprefix, jp))
        rad = averDeg('%s.rw%0.3f.rm1' % (fileprefix, jp))

        output.write('%f,%f,%f,%f\n' % (jp, nad, cad, rad))

    output.close()


def makeJP_AverDeg_Var_Plot(fileprefix, outputFilename):
    '''
    OUTPUT:
        JP, NOR_Aver_Deg_VAR, CW_Aver_Deg_VAR, RM1_Aver_Deg_VAR
    '''

    output = open(outputFilename, 'w')

    for i in range(1, 21):
        jp = i * 0.01
        nad = averDegVar('%s.rw%0.3f' % (fileprefix, jp))
        cad = averDegVar('%s.rw%0.3f.cw' % (fileprefix, jp))
        rad = averDegVar('%s.rw%0.3f.rm1' % (fileprefix, jp))

        output.write('%f,%f,%f,%f\n' % (jp, nad, cad, rad))

    output.close()

def makeJP_AverDeg_Bias_Plot(fileprefix, outputFilename, realVal):
    '''
    OUTPUT:
        JP, NOR_Aver_Deg_BIAS, CW_Aver_Deg_BIAS, RM1_Aver_Deg_BIAS
    '''

    output = open(outputFilename, 'w')

    for i in range(1, 21):
        jp = i * 0.01
        nad = averDegBias('%s.rw%0.3f' % (fileprefix, jp), realVal)
        cad = averDegBias('%s.rw%0.3f.cw' % (fileprefix, jp), realVal)
        rad = averDegBias('%s.rw%0.3f.rm1' % (fileprefix, jp), realVal)

        output.write('%f,%f,%f,%f\n' % (jp, nad, cad, rad))

    output.close()


if __name__ == '__main__':
    REAL_AVER_DEG = {
        'Amazon0505WCC.dat': 5.94642352207,
        'BerkStanWCC.dat': 10.0520035676,
        'cit-PatentsWCC.dat': 4.38661710037,
        'dblpWCC.dat': 3.66041751848,
        'EmailEuWCC.dat': 1.51190666809,
        'facebookWCC.dat': 12.8862632509,
        'flickrEdgesWCC.dat': 21.7591751797,
        'GnutellaWCC.dat': 2.36374098879,
        'GoogleWCC.dat': 5.01442156013,
        'Gowalla_edgesWCC.dat': 4.83403105941,
        'IMDBWCC.dat': 40.0918504396,
        'indexedFacebookWCC.dat': 7.13557100121,
        'NotreDameWCC.dat': 3.34667161966,
        'skitterWCC.dat': 6.54673920227,
        'Slashdot0902WCC.dat': 6.1365738487,
        'soc-Epinions1WCC.dat': 5.34732527643,
        'StanfordWCC.dat': 7.60749025522,
        'WikiTalkWCC.dat': 1.94925643158,
        'youtubeWCC.dat': 2.6325229758
    }
    for f in glob.glob('/Users/jeky/dataset/samples/*'):
        print 'analysing', f
        makeJP_AverDeg_Plot('/Users/jeky/dataset/samples_averd/' + os.path.basename(f), \
                            '/Users/jeky/dataset/samples_plot/aver_deg/' + os.path.basename(f))
        makeJP_AverDeg_Var_Plot('/Users/jeky/dataset/samples_averd/' + os.path.basename(f), \
                                '/Users/jeky/dataset/samples_plot/aver_deg_var/' + os.path.basename(f))
        makeJP_AverDeg_Bias_Plot('/Users/jeky/dataset/samples_averd/' + os.path.basename(f), \
                                 '/Users/jeky/dataset/samples_plot/aver_deg_bias/' + os.path.basename(f), \
                                 REAL_AVER_DEG[os.path.basename(f)])
        
