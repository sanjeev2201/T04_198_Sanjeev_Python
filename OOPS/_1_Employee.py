class Employee:
    # create employee
    def __init__(self, eid, emp_name, emp_sal):
        self.eid = eid
        self.emp_name = emp_name
        self.emp_sal = emp_sal

    # Retrieve emp
    def get_emp_info(self):
        print("Employee Details:", self.eid, self.emp_name, self.emp_sal)
        # 3. Update emp sal based on exp
        '''
            3. Give hike for employee based on experience
            Acceptance Criteria : 0 to 2 exp  => 5% hike
                                  2 to 3 exp  => 10% hike
                                  3 to 5 exp  => 20% hike
                                  5+          => 30% hike
        '''

    def Update_emp(self, exp):
        if 0 < exp < 2:
            hike = self.emp_sal * 5 / 100
            self.emp_sal = self.emp_sal + hike
        elif 2 <= exp < 3:
            hike = self.emp_sal * 10 / 100
            self.emp_sal = self.emp_sal + hike
        elif 3 <= exp < 5:
            hike = self.emp_sal * 20 / 100
            self.emp_sal = self.emp_sal + hike
        else:
            hike = self.emp_sal * 30 / 100
            self.emp_sal = self.emp_sal + hike
        print("Employee  after hike : ", self.eid, self.emp_name, self.emp_sal)


emp_1 = Employee(198, 'Sanjeev', 23000)
emp_1.get_emp_info()
emp_1.Update_emp(10)
emp_2 = Employee(161, 'Pawan', 35000)
emp_2.get_emp_info()
emp_2.Update_emp(3.5)
