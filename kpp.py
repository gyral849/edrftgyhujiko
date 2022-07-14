class Kpp ():
    def __init__(self, kpp, kpp_input=0, kpp_out=0, r_count=0):
        self.kpp_input = kpp_input
        self.kpp_out = kpp_out
        self.kpp = kpp
        self.r_count = r_count
    def r_kpp_in (self) :
        self.kpp_input += 1
    def r_kpp_out (self) :
        self.kpp_out += 1
    def nomer (self) :
        if self.kpp_input - self.kpp_out < 0:
            self.r_count = 0
        else:
            self.r_count = self.kpp_input - self.kpp_out
class worker() :
    def __init__(self, name, family, otchestvo, n_otdela, identificator):
        self.name = name
        self.family = family
        self.otchestvo = otchestvo
        self.n_otdela = n_otdela
        self.identificator = identificator
    def input_worker (self, _kpp):
        if self.n_otdela == _kpp.kpp:
            print('entered !!!! ', self.name, self.family, self.otchestvo)
            _kpp.r_kpp_in()
            _kpp.nomer()
    def job_out (self , _kpp):
        if self.n_otdela == _kpp.kpp:
            print('came out!!!', self.name, self.name, self.family, self.otchestvo)
            _kpp.r_kpp_out()
            _kpp.nomer()

kp = Kpp(1)
kp2 = Kpp(2)
kp3 = Kpp(3)


job1 = worker('lesha', 'leshenko', 'aleheevich', 2, 56)
job2 = worker('gosha', 'lesenko', 'aleh', 1, 35)
job3 = worker('edvard', 'petyshok', 'heevich', 3, 76)
job4 = worker('ramil', 'evgenyev', 'alevich', 2, 19)

job1.input_worker(kp2)
job3.input_worker(kp2)
job3.input_worker(kp3)
job1.input_worker(kp2)
job1.input_worker(kp3)
job2.input_worker(kp)
job4.input_worker(kp2)

count_job = kp.kpp_input + kp2.kpp_input + kp3.kpp_input

print(count_job)
print()
job1.job_out(kp2)
job1.job_out(kp)
job3.job_out(kp3)
job3.job_out(kp2)
job1.job_out(kp3)
job4.job_out(kp2)
job2.job_out(kp)
job4.job_out(kp2)

count_von = kp.kpp_out + kp2.kpp_out + kp3.kpp_out
print(count_von)