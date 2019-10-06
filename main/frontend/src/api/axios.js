import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

axios.defaults.baseURL = 'http://13.125.155.180:8000/api/';

const releaseApi = {
	login: 'rest-auth/login/',
	logout: 'rest-auth/logout/',
	registration: 'rest-auth/registration/',
	user: 'user/',
	profile: 'profiles/',
	surveys: 'surveys/',
	profileupdate: 'profileupdate/',
	stomach: 'surveys/stomach/',
};

function Login(loginObj) {
	return axios.post(releaseApi.login, loginObj);
}
function Logout(userInfo) {
	return axios.post(releaseApi.logout, userInfo);
}
function Signup(signupObj) {
	return axios.post(releaseApi.registration, signupObj);
}
function getMemberInfo(config) {
	return axios.get(releaseApi.user, config);
}
function getProfileInfo(config) {
	return axios.get(releaseApi.profile, config);
}
function getStomachInfo(stomachId, config) {
	const getStomachUrl = `${releaseApi.stomach}${stomachId}`;
	return axios.get(getStomachUrl, config);
}
function getSurveyHistory(config) {
	return axios.get(releaseApi.surveys, config);
}
function updateProfileInfo(config, update) {
	return axios.put(releaseApi.profileupdate, update, config);
}
function shootSurveyData(stomachData, config) {
	return axios.post(releaseApi.stomach, stomachData, config);
}

export {
	Login,
	Logout,
	Signup,
	getMemberInfo,
	getProfileInfo,
	getStomachInfo,
	getSurveyHistory,
	updateProfileInfo,
	shootSurveyData,
};
