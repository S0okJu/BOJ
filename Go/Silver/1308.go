package Silver

import (
	"fmt"
)

var DateCalc map[int]int = map[int]int{
	1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151,
	7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334,
}

type Date struct {
	Year  int
	Month int
	Day   int
}

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

// DayCalculator calculates the day of the year for a given date
func DayCalculator(date Date) int {
	day := DateCalc[date.Month] + date.Day
	if isLeapYear(date.Year) && date.Month > 2 {
		day += 1
	}
	return day
}

func Silver1308() {
	var date1, date2 Date
	fmt.Scanf("%d %d %d", &date1.Year, &date1.Month, &date1.Day)
	fmt.Scanf("%d %d %d", &date2.Year, &date2.Month, &date2.Day)

	if date2.Year-date1.Year > 1000 || (date2.Year-date1.Year == 1000 && (date2.Month > date1.Month || (date2.Month == date1.Month && date2.Day >= date1.Day))) {
		fmt.Println("gg")
		return
	}

	daysBetweenYears := 0
	for year := date1.Year; year < date2.Year; year++ {
		if isLeapYear(year) {
			daysBetweenYears += 366
		} else {
			daysBetweenYears += 365
		}
	}

	date1DayOfYear := DayCalculator(date1)
	date2DayOfYear := DayCalculator(date2)

	totalDays := daysBetweenYears + date2DayOfYear - date1DayOfYear
	fmt.Printf("D-%d\n", totalDays)
}
