#!/bin/bash

_version="1.0.3-docker"

self_file="$0"

_do_update="false"
_debug="false"

function _info {
	echo "$@"
}

function _debug {
	if [ "${_debug}" == "true" ]; then
		echo "$@"
	fi
}

function _newline {
	echo ""
}

function _file_download {
	local file="$1"
	local source_url="$2"

	curl -L -f -s -o "${file}" "${source_url}"
	curl_result=$?

	if [ "${curl_result}" != "0" ]; then
		_info "! download failed (bad URL or 404), skipping..."
		_newline
		return 1
	fi

	return 0
}

# options
while [[ "$#" -gt 0 ]]; do
	case $1 in
		--update) _do_update="true" ;;
		--debug) _debug="true" ;;
	esac
	shift
done

_info "> ${self_file}"
_newline

# ✅ DOCKER SAFE PATH
BLUEPRINTS_DIR="/config/blueprints"

if [ -d "${BLUEPRINTS_DIR}" ]; then
	cd "${BLUEPRINTS_DIR}" || exit 1
else
	_info "-! no blueprints dir found at ${BLUEPRINTS_DIR}"
	exit 1
fi

find . -type f -name "*.yaml" | while read file; do

	_info "> ${file}"

	blueprint_source_url=$(grep '^ *source_url: ' "${file}" | sed -e 's/^ *source_url: *//' -e 's/"//g' -e "s/'//g")

	if [ "${blueprint_source_url}" == "" ]; then
		_info "-! no source_url in file"
		_newline
		continue
	fi

	if [[ "${blueprint_source_url}" == *"github.com"* ]]; then
		blueprint_source_url=$(echo "${blueprint_source_url}" | sed \
			-e 's#https://github.com/#https://raw.githubusercontent.com/#' \
			-e 's#/blob/#/#')
	fi

	tempfile=$(mktemp)

	_file_download "${tempfile}" "${blueprint_source_url}"
	if [ $? -ne 0 ]; then
		_info "-! skipping ${file} due to download error"
		rm -f "${tempfile}"
		continue
	fi

	diff_result=$(diff "${file}" "${tempfile}")

	if [ "${diff_result}" == "" ]; then
		_info "-> blueprint up-2-date"
	else
		if [ "${_do_update}" == "true" ]; then
			cp "${tempfile}" "${file}"
			_info "-! blueprint updated!"
		else
			_info "-! blueprint changed (run with --update)"
		fi
	fi

	rm -f "${tempfile}"
	_newline

done

_info "Done."
