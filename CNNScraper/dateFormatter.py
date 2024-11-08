def formatDate(dateElement):
    dateFirstHalf = dateElement[1][4:]
    year = int(dateElement[2])

    monthNum = 0

    match dateFirstHalf[:dateFirstHalf.index(" ")]:
        case 'January':
            monthNum = 1
        case 'February':
            monthNum = 2
        case 'March':
            monthNum = 3
        case 'April':
            monthNum = 4
        case 'May':
            monthNum = 5
        case 'June':
            monthNum = 6
        case 'July':
            monthNum = 7
        case 'August':
            monthNum = 8
        case 'September':
            monthNum = 9
        case 'October':
            monthNum = 10
        case 'November':
            monthNum = 11
        case 'December':
            monthNum = 12

    return monthNum, year
