#ifndef STATS_FUNCTIONS_H
#define STATS_FUNCTIONS_H

float mean(std::vector<float> numbers);
float median(std::vector<float> numbers);
std::vector<float> mode(std::vector<float> numbers);
float lower_quartile(std::vector<float> numbers);
float upper_quartile(std::vector<float> numbers);

std::string print_mode(std::vector<float> numbers);

#endif
