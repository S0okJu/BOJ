package Silver

import (
	"fmt"
)

// DaysOfMonth : 각 월에 해당되는 일 수를 저장한다.
// 일 수가 고정되어 있으므로 미리 map 타입으로 정의한다.
var DaysOfMonth map[int]int = map[int]int{
	1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151,
	7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334,
}

type Date struct {
	Year  int
	Month int
	Day   int
}

// isLeapYear : 윤년인지 확인한다.
func isLeapYear(year int) bool {
	if year%4 == 0 {
		if year%100 == 0 {
			if year%400 == 0 {
				return true
			}
			return false
		}
		return true
	}
	return false
}

// DayCalculator : Date 구조체를 받아서 해당 날짜를 일 단위로 변환시킨다.
// 월, 일을 일 단위로 변환시킨다.
// DaysOfMonth 에서 2월의 경우 평년 28일을 기준으로 정했으며, 추후 윤년인 경우 1일을 더해준다.
func DayCalculator(date Date) int {
	day := DaysOfMonth[date.Month] + date.Day
	if isLeapYear(date.Year) && date.Month > 2 {
		day += 1
	}
	return day
}

func Silver1308() {
	// 1. today, dday을 입력받는다.
	var today, dday Date
	fmt.Scanf("%d %d %d", &today.Year, &today.Month, &today.Day)
	fmt.Scanf("%d %d %d", &dday.Year, &dday.Month, &dday.Day)

	// 2. 값의 차가 1000년이 넘는지 확인한다.
	if dday.Year-today.Year > 1000 || (dday.Year-today.Year == 1000 && (dday.Month > today.Month || (dday.Month == today.Month && dday.Day >= today.Day))) {
		fmt.Println("gg")
		return
	}

	// 3. 일 단위로 전환한다.
	// 3.1. today, dday 년 차이를 일 단위로 전환시킨다.
	daysBetweenYears := 0
	for year := today.Year; year < dday.Year; year++ {
		if isLeapYear(year) {
			daysBetweenYears += 366
		} else {
			daysBetweenYears += 365
		}
	}
	todayDayOfYear := DayCalculator(today)

	// 3.2. dday을 일 단위로 전환시킨다.
	ddayDayOfYear := DayCalculator(dday)

	// 4. today, dday의 차이를 계산한다.
	totalDays := (daysBetweenYears + ddayDayOfYear) - todayDayOfYear
	fmt.Printf("D-%d\n", totalDays)
}
