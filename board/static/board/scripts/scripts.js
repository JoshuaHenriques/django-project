function toggle(id) {
	const state = document.getElementById(id).style.display
	if (state == 'none') {
		document.getElementById(id).style.display = "block"
	}
	else { document.getElementById(id).style.display = "none" }
}