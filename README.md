# claude-actions-test

GitHub Actions から [Claude Code Action](https://github.com/anthropics/claude-code-action) を動かす検証用リポジトリです。

## 構成

```
.github/workflows/claude-actions.yml   # Claude Code によるPRレビュー用ワークフロー
.gitignore
```

## ワークフロー

`claude-actions.yml` は、プルリクエストに `claude-review` ラベルを付けると起動し、Claude がPRをレビューしてコメントを投稿します。
Claude の GitHub App は使わず、`GITHUB_TOKEN`（`github-actions[bot]` 名義）で動作します。

| トリガー | 条件 |
| --- | --- |
| `pull_request` (labeled) | 付けたラベルが `claude-review` |

## セットアップ

1. リポジトリの **Settings > Secrets and variables > Actions** に `CLAUDE_CODE_OAUTH_TOKEN`（`claude setup-token` で発行）を登録する。
2. リポジトリに `claude-review` ラベルを作成する。
3. レビューしてほしいPRに `claude-review` ラベルを付ける。再レビューはラベルを外して付け直す。
