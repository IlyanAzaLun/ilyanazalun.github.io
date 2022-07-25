---
title: Ajax Request Datatabels
tags: [Ajax, Data Tabels]
style: 
color: 
description: Request to the server for each draw of the information on the page.
---

Source: [DataTables](https://datatables.net/manual/server-side#Example-data)

Processing in datatabels is enabled thought use of the `serverSide: true` option, and use
the `ajax: 'url'` :

## Example
### View
```
let tabel = $('#example').DataTabel({
	serverSide: true,
	ajax: {
        // if can using API to get this data.?
		'url' : "path/file/func",
        'type': "POST"
	},
    // Name Column
    columns: [{
      data: "id"
    },{
      data: "item_code",
    },{
      data: "item_name",
    },{
      data: "category"
    },{
      data: "brand"
    },{
      data: "brands"
    },{
      data: 'item_quantity',
    },{
      data: 'item_broken',
    },{
      data: 'weight',
    },{
      data: 'item_unit',
    },{
      data: "item_capital_price",
    },{
      data: "item_selling_price",
    },{
      data: "note"
    },{
      data: "id",
    },
  ]
})
```
on file function

### Controller
```
function func(){
	$response = array();

    $postData = $this->input->post();

    ## Read value
    $draw = $postData['draw'];
    $start = $postData['start'];
    $rowperpage = $postData['length']; // Rows display per page
    $columnIndex = $postData['order'][0]['column']; // Column index
    $columnName = $postData['columns'][$columnIndex]['data']; // Column name
    $columnSortOrder = $postData['order'][0]['dir']; // asc or desc
    $searchValue = $postData['search']['value']; // Search value

    ## Total number of records without filtering
    $this->db->select('count(*) as allcount');
    $records = $this->db->get('items')->result();
    $totalRecords = $records[0]->allcount;

    ## Total number of record with filtering
    $this->db->select('count(*) as allcount');
    if ($searchValue != '') {
        // EXAMPLE //
        $this->db->like('item_name', $searchValue, 'both');
        $this->db->or_like('item_code', $searchValue, 'both');
        $this->db->or_like('category', $searchValue, 'both');
    }
    $records = $this->db->get('items')->result();
    $totalRecordwithFilter = $records[0]->allcount;

    ## Fetch records
    $this->db->select('*');
    if ($searchValue != '') {
        // EXAMPLE //
        $this->db->like('item_name', $searchValue, 'both');
        $this->db->or_like('item_code', $searchValue, 'both');
        $this->db->or_like('category', $searchValue, 'both');
    }
    $this->db->order_by($columnName, $columnSortOrder);
    $this->db->limit($rowperpage, $start);
    $records = $this->db->get('items')->result();

    $data = array();

    foreach ($records as $record) {

        $data[] = array(
            // EXAMPLE // Name Column
            "id" => $record->id,
            "item_code" => $record->item_code,
            "item_name" => $record->item_name,
            "category" => $record->category,
            "item_quantity" => $record->quantity,
            "item_broken" => $record->broken,
            "item_unit" => $record->unit,
            "item_capital_price" => $record->capital_price,
            "item_selling_price" => $record->selling_price,
            "note" => $record->note,
            "is_active" => $record->is_active,
        );
    }

    ## Response
    $response = array(
        "draw" => intval($draw),
        "iTotalRecords" => $totalRecords,
        "iTotalDisplayRecords" => $totalRecordwithFilter,
        "aaData" => $data
    );
    $this->output->set_content_type('application/json')->set_output(json_encode($response));
}
```
```

```
add event on datatabels draw,
```
tabel.on('draw', function(){
  // your function
})
```