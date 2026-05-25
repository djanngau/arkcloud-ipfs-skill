from __future__ import annotations

import json
import io
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "skills" / "arkcloud-ipfs" / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

import arkcloud_common  # noqa: E402
import arkcloud_upload  # noqa: E402


class ArkcloudCommonTests(unittest.TestCase):
    def test_endpoint_normalizes_slashes(self) -> None:
        self.assertEqual(
            arkcloud_common.endpoint("https://file.arklink.hk/", "/api/health"),
            "https://file.arklink.hk/api/health",
        )

    def test_require_env_fails_without_value(self) -> None:
        with mock.patch.dict(os.environ, {}, clear=True):
            with mock.patch("sys.stdout", new_callable=io.StringIO):
                with self.assertRaises(SystemExit):
                    arkcloud_common.require_env("ARKCLOUD_UPLOAD_TOKEN")


class ArkcloudUploadTests(unittest.TestCase):
    def test_form_filename_escapes_unsafe_characters(self) -> None:
        self.assertEqual(
            arkcloud_upload.form_filename('a"b\r\nc\\d.txt'),
            'a\\"b__c\\\\d.txt',
        )

    def test_empty_folder_upload_fails_before_network(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch("sys.stdout", new_callable=io.StringIO):
                with self.assertRaises(SystemExit):
                    arkcloud_upload.multipart_folder(Path(tmp))

    def test_normalize_result_expands_relative_short_url(self) -> None:
        result = arkcloud_upload.normalize_result(
            {"cid": "bafy", "short_url": "/f/abc"},
            "https://file.arklink.hk",
        )
        self.assertEqual(result["url"], "https://file.arklink.hk/f/abc")
        self.assertTrue(result["ok"])

    def test_fail_prints_json_payload(self) -> None:
        with mock.patch("sys.stdout") as stdout:
            with self.assertRaises(SystemExit):
                arkcloud_common.fail("boom", code=9, status=500)
        payload = json.loads("".join(call.args[0] for call in stdout.write.call_args_list))
        self.assertEqual(payload["error"], "boom")
        self.assertEqual(payload["status"], 500)


if __name__ == "__main__":
    unittest.main()
