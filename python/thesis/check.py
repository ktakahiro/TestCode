import scipy.misc as scm

class Calculation:
    @staticmethod
    def correct(p, cor, rat):
        return scm.comb(cor + rat, cor, 1) * pow(p, rat) * pow(1 - p, cor)

    @staticmethod
    def fail(p, n, s, k, cor, rat):
        # print("fail : {0}C{1}*{2}C{3}*{4}C{5}*{6}^{7}*{8}^{9}/{10}C{11})" \
        #      .format(n - s, k - s, c, n - k, r - 1, k, p, k - s, 1 - p, s, c + r - 1, n))
        return scm.comb(n - s, k - s, 1) * scm.comb(cor, n - k, 1) * scm.comb(rat - 1, k, 1) * pow(p, k - s) \
               * pow(1 - p, s) / scm.comb(cor + rat - 1, n, 1)

    @staticmethod
    def success(p, n, f, k, cor, rat):
        # print("success : {0}C{1}*{2}C{3}*{4}C{5}*{6}^{7}*{8}^{9}/{10}C{11})" \
        #      .format(n - f, k - f, cor, n - k, rat - 1, k, p, k - f, 1 - p, f, cor + rat - 1, n))
        return scm.comb(n - f, k - f, 1) * scm.comb(cor, n - k, 1) * scm.comb(rat - 1, k, 1) \
               * pow(p, f) * pow(1 - p, k - f) / scm.comb(cor + rat - 1, n, 1)

    def optimal_move(self, p, f, s, check):
        n = s + f
        p_check = 0
        p_correct = 0
        for selfish in (0, (check - 1) / 2 + 1):
            suc = 0
            fai = 0
            for j in range(s, n + 1):
                fai += self.fail(p, n, s, j, check - selfish, selfish)
            for i in range(n - s, n + 1):
                suc += self.success(p, n, f, i, check - selfish, selfish)

            temp_p_correct = self.correct(p, check - selfish, selfish)
            p_correct += temp_p_correct
            # no more rational robot
            if (suc + fai) == 0:
            #    print("suc + fai = 0 at {0} {1} {2}".format(selfish,f,s))
                if s > f:
                    p_check += 1 * temp_p_correct
            else:
                p_check += suc / float(suc + fai) * temp_p_correct

        if float(max([p_check, 1 - p_check]) / p_correct) > max(p, 1 - p):
            if p_check >= 1 - p_check:
                return True
            else:
                return False
        else:
            if (1 - p) >= p:
                return True
            else:
                return False

    def calc_prob(self, p, f, s, check):
        n = s + f
        p_check = 0
        p_correct = 0

        for selfish in (0, (check - 1) / 2 + 1):
            suc = 0
            fai = 0
            for j in range(s, n + 1):
                fai += self.fail(p, n, s, j, check - selfish, selfish)
            for i in range(n - s, n + 1):
                suc += self.success(p, n, f, i, check - selfish, selfish)
            # no more rational robot
            temp_p_correct = self.correct(p, check - selfish, selfish)
            p_correct += temp_p_correct
            if (suc + fai) == 0:
            #    print("suc + fai = 0 at {0} {1} {2}".format(selfish,f,s))
                p_check += 1 * temp_p_correct
            else:
                p_check += float(max([suc, fai])) / float(suc + fai) * temp_p_correct

        return p_check / p_correct

    @staticmethod
    def Binomial(k, w, p):
        return float(scm.comb(w, k, 1) * pow(p, k) * pow(1 - p, w - k))

p = 0.3
check = 5

for n in range(check):
    print("{0} ".format(n+1), end="")
    for s in range(5):
        if (n-s >= 0):
            p_check = Calculation().calc_prob(p,n-s,s,5)
            print("& {:0<7} ".format(round(p_check,5)), end="")
        else:
            print("& - ", end="")
    print(" \\\\ \hline")
