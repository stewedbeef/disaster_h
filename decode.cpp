#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int convert(const std::string_view s) {
	int n = 0;
	bool negative = false;
	for (auto c : s) {
		if (c == '-') {
			negative = true;
		} else if ('0' <= c && c <= '9') {
			n = n * 10 + c - '0';
		} else if (c != ' ') {
			std::cerr << "Detected stray non numeric char " << c << '\n';
		}
	}
	return negative ? -n : n;
}

std::vector<int> decode(const std::string_view input) {
	const int year = convert(input.substr(0, 4));
	const int month = convert(input.substr(4, 2));
	const int day = convert(input.substr(6, 2));
	const int hour = convert(input.substr(8, 4));

	const int lat = convert(input.substr(12, 5));
	int lon = convert(input.substr(17, 6));
	if (lon > 18000) {
		lon -= 36000;
	}

	if (1050 >= lat || lat >= 4680) {
		return std::vector<int>{};
	}
	if (-9500 >= lon || lon >= -2275) {
		return std::vector<int>{};
	}

	const int sst = convert(input.substr(85, 4));
	const int slp = convert(input.substr(59, 5));
	const int w = convert(input.substr(50, 3));
	const int at = convert(input.substr(69, 4));
	const int ww = convert(input.substr(56, 2));
	const int w1 = convert(input.substr(58, 1));
	const int ppp = convert(input.substr(65, 3));
	const int wd = convert(input.substr(96, 2));
	const int wp = convert(input.substr(98, 2));
	const int wh = convert(input.substr(100, 2));
	const int sd = convert(input.substr(102, 2));
	const int sp = convert(input.substr(104, 2));
	const int sh = convert(input.substr(106, 2));
	const int c1 = convert(input.substr(43, 2));

	std::vector<int> output{
		year,
		month,
		day,
		hour,
		lat,
		lon,
		sst,
		slp,
		w,
		at,
		ww,
		w1,
		ppp,
		wd,
		wp,
		wh,
		sd,
		sp,
		sh,
		c1
	};
	return output;
}

int main(int argc, char *argv[]) {
	if (argc != 3) {
		std::cerr << "program input output\n";
		return 1;
	}

	std::ifstream in{argv[1]};
	std::ofstream of{argv[2]};
	if (in.fail()) {
		std::cerr << "In Fail\n";
		return 1;
	}
	if (of.fail()) {
		std::cerr << "Out fail\n";
		return 1;
	}
	constexpr std::string_view comma{", "};

	std::string buffer;
	while (std::getline(in, buffer)) {
		std::vector<int> out = decode(buffer);
		if (out.empty()) {
			continue;
		}
		int last = out.back();
		out.pop_back();
		for (auto x : out) {
			of << x << comma;
		}
		of << last << '\n';
	}
	return 0;
}
