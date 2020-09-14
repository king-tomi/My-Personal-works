class Student {

    constructor(name,dob,regNo) {
        this.name = name;
        this.dob = dob;
        this.regNo = regNo;
    }

    name (){
        return this.name;
    }

    dob() {
        return this.dob;
    }

    regNo() {
        return this.regNo;
    }
}

const studentGroup  = (students) => {
    let output = [];
    let temp = [];
    for (let j = 0; j < students.length; j++) {
        for(let i = 0; i < 3; i++) {
            choice = Math.floor(Math.random() * (students.length - 0) + 0);
            let prev = null;
            student = students[choice];
            if (prev === null) {
                temp.push(student);
            }
            else if (prev === student) {
                choice = Math.floor(Math.random() * (students.length - 0) + 0);
                student = students[choice];
                temp.push(student);
            }
            else {
                temp.push(student);
            }
            prev = student;
        }
        output.push(temp); 
    }
}