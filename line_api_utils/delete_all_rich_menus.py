from dotenv import load_dotenv
import os
import requests
from rich.console import Console
from rich.table import Table

def main():
    console = Console()
    load_dotenv()

    # 環境変数からアクセストークンを取得
    CHANNEL_ACCESS_TOKEN = os.getenv('CHANNEL_ACCESS_TOKEN')

    if not CHANNEL_ACCESS_TOKEN:
        console.print("[bold red]エラー:[/bold red] 環境変数からCHANNEL_ACCESS_TOKENが見つかりません。")
        return

    headers = {
        'Authorization': f'Bearer {CHANNEL_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }

    # リッチメニューのリストを取得
    console.print("[bold]リッチメニューのリストを取得しています...[/bold]")
    response = requests.get('https://api.line.me/v2/bot/richmenu/list', headers=headers)

    if response.status_code != 200:
        console.print(f"[bold red]リッチメニューの取得エラー:[/bold red] {response.status_code} {response.text}")
        return

    data = response.json()

    richmenus = data.get('richmenus', [])

    if not richmenus:
        console.print("[bold green]リッチメニューは見つかりませんでした。[/bold green]")
        return

    # リッチメニューのリストを表示
    table = Table(title="リッチメニュー一覧")
    table.add_column("ID", style="cyan")
    table.add_column("名前", style="magenta")
    table.add_column("チャットバーのテキスト", style="green")
    table.add_column("選択中", style="yellow")

    for rm in richmenus:
        table.add_row(
            rm.get('richMenuId', ''),
            rm.get('name', ''),
            rm.get('chatBarText', ''),
            str(rm.get('selected', ''))
        )

    console.print(table)

    # 削除確認
    console.print("[bold red]すべてのリッチメニューを削除しますか？[/bold red] (yes/no)")
    confirm = input()

    if confirm.lower() != 'yes':
        console.print("[bold]操作がキャンセルされました。[/bold]")
        return

    # 各リッチメニューを削除
    for rm in richmenus:
        rich_menu_id = rm.get('richMenuId')
        if rich_menu_id:
            console.print(f"リッチメニュー [cyan]{rich_menu_id}[/cyan] を削除しています...")
            del_response = requests.delete(f'https://api.line.me/v2/bot/richmenu/{rich_menu_id}', headers=headers)
            if del_response.status_code != 200:
                console.print(f"[bold red]リッチメニュー {rich_menu_id} の削除エラー:[/bold red] {del_response.status_code} {del_response.text}")
            else:
                console.print(f"[bold green]リッチメニュー {rich_menu_id} を削除しました。[/bold green]")

    console.print("[bold green]すべてのリッチメニューが削除されました。[/bold green]")

if __name__ == "__main__":
    main()